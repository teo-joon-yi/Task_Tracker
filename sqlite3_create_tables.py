import sqlite3

connection = sqlite3.connect("tasks.db") #connects to task database

#creates task table
connection.execute('''CREATE TABLE IF NOT EXISTS Tasks(
TaskID INTEGER PRIMARY KEY AUTOINCREMENT,
Title TEXT,
Description TEXT,
AssignedMember TEXT,
CreatedBy TEXT,
Priority TEXT,
Status TEXT
)''')

#create people table
connection.execute('''CREATE TABLE IF NOT EXISTS People(
PeopleID INTEGER PRIMARY KEY AUTOINCREMENT,
Name TEXT
)''') #if we create a login feature can add password or smth

#create project table
connection.execute('''CREATE TABLE IF NOT EXISTS Project(
ProjectID INTEGER PRIMARY KEY AUTOINCREMENT,
TaskID INTEGER,
PeopleID INTEGER,

FOREIGN KEY(TaskID) REFERENCES Tasks(TaskID),
FOREIGN KEY(PeopleID) REFERENCES People(PeopleID)
)''')

connection.close()
