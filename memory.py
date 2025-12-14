import sqlite3
import os

DB_PATH = "data/todos.db"
os.makedirs("data", exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY,
    task TEXT,
    done INTEGER DEFAULT 0
)
""")
conn.commit()

def get_todos():
    cursor.execute("SELECT task FROM todos WHERE done = 0")
    return [row[0] for row in cursor.fetchall()]

