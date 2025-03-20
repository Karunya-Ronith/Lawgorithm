import sqlite3

conn = sqlite3.connect("legal_data.db")
cursor = conn.cursor()

s = cursor.execute('''
SELECT title FROM legal_docs
''')

print(s.fetchall())