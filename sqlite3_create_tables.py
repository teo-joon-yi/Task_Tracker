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

PRIMARY KEY(Title)
FOREIGN KEY(AssignedMember) REFERENCES People(Name)
FOREIGN KEY(CreatedBy) REFERENCES People(Name)

)''')

#create people table
connection.execute('''CREATE TABLE IF NOT EXISTS People(
Name TEXT
)''') #if we create a login feature can add password or smth

connection.close()
