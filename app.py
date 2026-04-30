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
    connection.commit()
    connection.close()

def delete_person(name):
    connection = sqlite3.connect("tasks.db")
    connection.execute('''DELETE FROM People WHERE Name = ?''', (name,))
    connection.commit()
    connection.close()

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

def update_task(taskname, newvalue): #e.g. if we're updating status from In Progress to complete the parameters shld be (taskname, "Status", "Complete")
    connection = sqlite3.connect("tasks.db")
    connection.execute('''UPDATE Tasks SET Status = ? WHERE Title = ?''', (newvalue, taskname))
    connection.commit()
    connection.close()
    
def delete_task(taskname):
  connection = sqlite3.connect("tasks.db")
  connection.execute('''DELETE FROM Tasks WHERE Title = ?''', (taskname,))
  connection.commit()
  connection.close()

def people_dict():
    connection = sqlite3.connect("tasks.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.execute('''SELECT Name FROM People''')
    peoplelist = []
    for item in cursor:
        peoplelist.append(dict(item))
        
    connection.close()

    return peoplelist

def people_list():
    connection = sqlite3.connect("tasks.db")
    cursor = connection.execute('''SELECT Name FROM People''')
    peoplelist = []

    for item in cursor:
        peoplelist.append(item[0])

    return peoplelist
    

def all_tasks():
    connection = sqlite3.connect("tasks.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.execute('''SELECT * FROM Tasks''')

    filterlist = []
    for row in cursor:
        filterlist.append(dict(row))

    connection.close()
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
        cursor = all_tasks()
        people = people_dict()
        return render_template("home.html", cursor = cursor, person = people)
    else: #post
        #delete task
        taskname = request.form.get("taskNameDelete")

        #new task
        newname = request.form.get('name')     
        description = request.form.get('description')
        peopleInvolved = request.form.get('peopleInvolved')
        creator = request.form.get('creator')
        status = request.form.get('status')

        #update task
        status_update = request.form.get("taskStatusUpdate")
        name = request.form.get("taskNameUpdate")

        #login
        username = request.form.get("username")

        cursor = all_tasks()
        people = people_dict()
        
        if taskname:
            delete_task(taskname)
            return render_template("home.html", cursor = all_tasks(), person = people_dict())

        elif newname:
            insert_task(newname, description, peopleInvolved, creator,status)
            return render_template("home.html", cursor = all_tasks(), person = people_dict())
        
        elif status_update:
            update_task(name, status_update)
            return render_template("home.html", cursor = all_tasks(), person = people_dict())

        elif username:
            peoplelist = people_list()
            if username not in peoplelist:
                add_people(username)

            return render_template("home.html", cursor = all_tasks(), person = people_dict())

@app.route('/newtask/')
def new_task():
    data = people_list()
    return render_template("newtask.html", data = data)

@app.route('/login/')
def new_person():
    return render_template("login.html")

if __name__ == '__main__':
    app.run()
