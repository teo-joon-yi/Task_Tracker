import sqlite3
def insert_task(title, desc, assignedmember, createdby, priority="Low", status="In Progress"):
  connection.execute('''INSERT INTO Tasks(Title, Description, AssignedMember, CreatedBy, Priority)
VALUES(?,?,?,?,?)''', (title, desc, assignedmember, createdby, priority, status))
  return True

def filter_task(, )

connection.close()
