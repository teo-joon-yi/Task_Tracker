import sqlite3
def insert_task(title, desc, assignedmember, createdby, status="In Progress", priority="Low"):
  connection = sqlite3.connect("tasks.db")
  connection.execute('''INSERT INTO Tasks(Title, Description, AssignedMember, CreatedBy, Priority)
VALUES(?,?,?,?,?)''', (title, desc, assignedmember, createdby, priority, status))
  connection.close()
  return True

def filter_task(filterby, value):
  connection = sqlite3.connect("tasks.db")
  cursor = connection.execute('''SELECT * FROM Tasks WHERE ? = ?''', (filterby, value))
  connection.close()

  
