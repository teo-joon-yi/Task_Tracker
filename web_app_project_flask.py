import sqlite3

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
