import sqlite3
def insert_task(title, desc, assignedmember, createdby, status="In Progress", priority="Low"):
  connection = sqlite3.connect("tasks.db")
  try: 
    connection.execute('''INSERT INTO Tasks(Title, Description, AssignedMember, CreatedBy, Priority)
    VALUES(?,?,?,?,?)''', (title, desc, assignedmember, createdby, priority, status))
    connection.commit()
    connection.close()
    return True
  except: #task already exists
    return False

def filter_task(filterby, value):
  connection = sqlite3.connect("tasks.db")
  cursor = connection.execute('''SELECT * FROM Tasks WHERE ? = ?''', (filterby, value)).fetchall() 
  connection.close()
  return cursor

def update_task(taskname, updateby, newvalue): #e.g. if we're updating status from In Progress to complete the parameters shld be (taskname, "Status", "Complete")
  connection = sqlite3.connect("tasks.db")
  connection.execute('''UPDATE TABLE Tasks SET ? = ? WHERE Title = ?''', (updateby, newvalue, taskname))
  connction.commit()
  connection.close()

def delete_task(taskname):
  connection = sqlite3.connect("tasks.db")
  connection.execute('''DELETE FROM Tasks WHERE Title = ?''', (taskname,))
  connection.commit()
  connection.close()

  
