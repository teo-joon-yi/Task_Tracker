from flask import Flask, render_template, request
import sqlite3

connection = sqlite3.connect("tasks.db") #connects to task database

#creates task table
connection.execute('''CREATE TABLE IF NOT EXISTS Tasks(
Title TEXT,
Description TEXT,
AssignedMember TEXT,
CreatedBy TEXT,
Priority TEXT,
Status TEXT,

PRIMARY KEY(Title),
FOREIGN KEY(AssignedMember) REFERENCES People(Name),
FOREIGN KEY(CreatedBy) REFERENCES People(Name)

)''')

#create people table
connection.execute('''CREATE TABLE IF NOT EXISTS People(
Name TEXT,

PRIMARY KEY(Name)
)''') #if we create a login feature can add password or smth

connection.close()

def add_people(name):
    connection = sqlite3.connect("tasks.db")
    connection.execute('''INSERT INTO People(Name) VALUES(?)''', (name,))
    return True



def insert_task(title, desc, assignedmember, createdby, status="In Progress", priority="Low"):
    connection = sqlite3.connect("tasks.db")
    try:
        connection.execute('''INSERT INTO Tasks(Title, Description, AssignedMember, CreatedBy, Priority, Status)
        VALUES(?,?,?,?,?,?)''', (title.strip().capitalize(), desc, assignedmember.strip().capitalize(), createdby.strip().capitalize(), priority, status))
        connection.commit()
        connection.close()
        return True
    except: #task already exists
        return False


def filter_task(filterby, value):
    connection = sqlite3.connect("tasks.db")
    value = value.strip().capitalize()
    
    if filterby=="Title":
        cursor = connection.execute('''SELECT * FROM Tasks WHERE Title = ?''', (value,)).fetchall()
    elif filterby=="Description":
        cursor = connection.execute('''SELECT * FROM Tasks WHERE Description = ?''', (value,)).fetchall()
    elif filterby == "AssignedMember":
        cursor = connection.execute('''SELECT * FROM Tasks WHERE AssignedMember= ?''', (value,)).fetchall()
    elif filterby == "CreatedBy":
        cursor = connection.execute('''SELECT * FROM Tasks WHERE CreatedBy= ?''', (value,)).fetchall()
    elif filterby == "Priority":
        cursor = connection.execute('''SELECT * FROM Tasks WHERE Priority= ?''', (value,)).fetchall()
    elif filterby == "Status":
        cursor = connection.execute('''SELECT * FROM Tasks WHERE Status= ?''', (value,)).fetchall()
    connection.close()
    
    filterlist = []
    for tup in cursor:
        tuplist = []
        for item in tup:
            tuplist.append(item)
        filterlist.append(tuplist)
    
    return filterlist

def update_task(taskname, updateby, newvalue): #e.g. if we're updating status from In Progress to complete the parameters shld be (taskname, "Status", "Complete")
    connection = sqlite3.connect("tasks.db")
    newvalue = newvalue.strip().capitalize()
    
    if updateby=="Title":
        connection.execute('''UPDATE Tasks SET Title = ? WHERE Title = ?''', (newvalue, taskname))
        connection.commit()
        return True
    elif updateby=="Description":
        connection.execute('''UPDATE Tasks SET Description = ? WHERE Title = ?''', (newvalue, taskname))
        connection.commit()
        return True
    elif updateby == "AssignedMember":
        connection.execute('''UPDATE Tasks SET AssignedMember = ? WHERE Title = ?''', (newvalue, taskname))
        connection.commit()
        return True
    elif updateby == "CreatedBy":
        connection.execute('''UPDATE Tasks SET CreatedBy = ? WHERE Title = ?''', (newvalue, taskname))
        connection.commit()
        return True
    elif updateby == "Priority":
        connection.execute('''UPDATE Tasks SET Priority = ? WHERE Title = ?''', (newvalue, taskname))
        connection.commit()
        return True
    elif updateby == "Status":
        connection.execute('''UPDATE Tasks SET Status = ? WHERE Title = ?''', (newvalue, taskname))
        connection.commit()
        return True
    else:
        return False
    connection.close()
    
def delete_task(taskname):
  connection = sqlite3.connect("tasks.db")
  connection.execute('''DELETE FROM Tasks WHERE Title = ?''', (taskname,))
  connection.commit()
  connection.close()

def people_list():
    connection = sqlite3.connect("tasks.db")
    cursor = connection.execute('''SELECT Name FROM People''').fetchall()

    peoplelist = []
    for item in cursor:
        peoplelist.append(item[0])

    return peoplelist

def all_tasks():
    connection = sqlite3.connect("tasks.db")
    cursor = connection.execute('''SELECT * FROM Tasks''').fetchall()
    connection.close()

    filterlist = []
    for tup in cursor:
        tuplist = []
        for item in tup:
            tuplist.append(item)
        filterlist.append(tuplist)
    
    return filterlist

try:
    add_people("Joon Yi")
    add_people("Rae Lynn")
    add_people("Deeksha")
    add_people("Josephine")
    add_people("Mr Lai")
    
    insert_task("Buy ingredients", "buy flour, eggs and sugar", "Joon Yi", "Mr Lai")
    insert_task("Bake cookies", "https://www.allrecipes.com/recipe/10813/best-chocolate-chip-cookies/ link to cookie recipe", "Rae Lynn", "Deeksha")
    insert_task("Clean up", "clean up workspace after baking cookies", "Josephine", "Mr Lai")
except:
    pass


app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def home():
    if request.method=="GET":
        return render_template("home.html")
    else: #post
        #filter submit
        status = request.form.get("status-selected")
        priority = request.form.get("priority-selected")
        person = request.form.get("person-selected")

        #delete submit
        taskname = request.form.get("TaskName")
        
        
        if status:
            cursor = filter_task("Status", status)
            return render_template("home.html", cursor = cursor)

        elif priority:
            cursor = filter_task("Priority", priority)
            return render_template("home.html", cursor = cursor)

        elif person:
            cursor = filter_task("AssignedMember", person)
            return render_template("home.html", cursor = cursor)

        elif taskname:
            delete_task(taskname)
            return render_template("home.html")        

@app.route('/newtask/', methods = ["POST", "GET"])
def new_task():
    if request.method == 'POST':    
        name = request.form['name']     
        description = request.form['description']
        peopleInvolved = request.form['peopleInvolved']
        creator = request.form['creator']
        status = request.form['status']

        insert_task(name, description, peopleInvolved, creator,status)
        return render_template("home.html")

    else:
        return render_template("newtask.html")
