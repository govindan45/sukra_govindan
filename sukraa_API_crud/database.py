import sqlite3

def get_db_connection():
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS Books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            published_date TEXT NOT NULL,
            isbn TEXT UNIQUE NOT NULL,
            page_count INTEGER,
            cover TEXT,
            language TEXT
        )
    ''')
    conn.commit()
    conn.close()
