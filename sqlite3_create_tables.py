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
)''')

#create people table
connection.execute('''CREATE TABLE IF NOT EXISTS People(
Name TEXT
)''') #if we create a login feature can add password or smth

#create project table
connection.execute('''CREATE TABLE IF NOT EXISTS Project(
ProjectID INTEGER PRIMARY KEY AUTOINCREMENT,
Title INTEGER,
Name INTEGER,

FOREIGN KEY(Title) REFERENCES Tasks(Title),
FOREIGN KEY(Name) REFERENCES People(Name)
)''')

connection.close()
