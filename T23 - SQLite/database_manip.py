""" Module for SQLlite3"""
import sqlite3
# Create or opens a file called database with SQLite3 DB

db = sqlite3.connect('database.db')

# Creating a table
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE python_programming(id INTEGER PRIMARY KEY, name TEXT,
                        grade INTEGER)
''')
db.commit()

# data to be inserted
students = [
    (55, 'Carl Davis', 61),
    (66, 'Dennis Fredrickson', 88),
    (77, 'Jane Richards', 78),
    (12, 'Peyton Sawyer', 45),
    (2, 'Lucas Brooke', 99)
]

cursor.executemany('''INSERT INTO python_programming(id, name, grade)
                  VALUES(?,?,?)''', students)
print('First users inserted')

# Commit the transaction
db.commit()

# Select all records with a grade between 60 and 80
cursor.execute('''
               SELECT id, name, grade FROM python_programming
               WHERE grade BETWEEN ? AND ?
               ''', (60, 80))
db.commit()

# Change Carl Davis's grade to 65
grade = 65
name = "Carl Davis"
cursor.execute('''UPDATE python_programming SET grade = ? WHERE name = ?
               ''', (grade, name))
db.commit()
# Delete Dennis Fredrickson's row
cursor.execute('''DELETE FROM python_programming WHERE name = ? ''',
               ('Dennis Fredrickson',))
db.commit()
# Change the grade of all students with id greater than 55 to the grade 80
cursor.execute('''UPDATE python_programming SET grade = ? WHERE id > ?
               ''', (80, 55))
db.commit()

db.close()
