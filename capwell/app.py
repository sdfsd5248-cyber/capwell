from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Function to get a database connection
def get_db_connection():
    conn = sqlite3.connect('my_website.db')
    conn.row_factory = sqlite3.Row  # This makes the data accessible by column name
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    # Execute a query to get data from your table
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('test(black).html', users=users)

if __name__ == '__main__':
    app.run(debug=True)