import sqlite3



connection = sqlite3.connect("notes.db")

connection.execute(""" 
                   CREATE TABLE IF NOT EXISTS notes (
                   id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   text TEXT
                   ) 
                   """)

connection.commit()
connection.close()