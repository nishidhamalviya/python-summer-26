import sqlite3
# database connected
# 1. Connect to a database (creates 'example.db' if it doesn't exist)
connection = sqlite3.connect('example.db')
cursor = connection.cursor()

# 2. Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
''')

# 3. Insert data
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 25))

# 4. Save (commit) changes
connection.commit()

# 5. Query the data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")

# 6. Close the connection
connection.close()
