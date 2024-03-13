import sqlite3

connection = sqlite3.connect("mydata.db")

cursor = connection.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS persons (
    username TEXT, 
    password TEXT
)
"""
)

connection.commit()
connection.close()
