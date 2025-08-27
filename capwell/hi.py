import sqlite3

conn = sqlite3.connect('my_website.db')
cursor = conn.cursor()

# Create the users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    );
''')

# Insert some sample data
cursor.execute("INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com')")
cursor.execute("INSERT INTO users (name, email) VALUES ('Bob', 'bob@example.com')")

conn.commit()
conn.close()

print('Database initialized and sample data added.')