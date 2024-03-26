
import sqlite3

def create_connection():
    connection = sqlite3.connect('datab.db')
    return connection

def create_suggestions_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS suggestions (
                        id INTEGER PRIMARY KEY,
                        user_id INTEGER,
                        suggestion TEXT)''')
    connection.commit()
    connection.close()

def save_suggestion(user_id, suggestion):
    conn = sqlite3.connect('datab.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO suggestions (user_id, suggestion) VALUES (?, ?)", (user_id, suggestion))
    conn.commit()
    conn.close()
