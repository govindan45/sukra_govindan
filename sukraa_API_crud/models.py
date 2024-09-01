from database import get_db_connection
import sqlite3


def create_book(title, author, published_date, isbn, page_count, cover, language):
    conn = get_db_connection()
    try:
        conn.execute('''
            INSERT INTO Books (title, author, published_date, isbn, page_count, cover, language)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (title, author, published_date, isbn, page_count, cover, language))
        conn.commit()
    except sqlite3.IntegrityError as e:
        conn.close()
        print(f"IntegrityError: {e}")
        raise ValueError('ISBN must be unique.')

def get_book(book_id):
    conn = get_db_connection()
    book = conn.execute('SELECT * FROM Books WHERE id = ?', (book_id,)).fetchone()
    conn.close()
    return book

def get_books(filters):
    conn = get_db_connection()
    query = 'SELECT * FROM Books WHERE 1=1'
    params = []
    if 'author' in filters:
        query += ' AND author LIKE ?'
        params.append(f"%{filters['author']}%")
    if 'published_date' in filters:
        query += ' AND published_date LIKE ?'
        params.append(f"%{filters['published_date']}%")
    if 'language' in filters:
        query += ' AND language LIKE ?'
        params.append(f"%{filters['language']}%")
    books = conn.execute(query, params).fetchall()
    conn.close()
    return books

# get All books without Filters 

def getAllBooks():
    conn = get_db_connection()
    query = "SELECT * FROM Books"
    books = conn.execute(query).fetchall()
    conn.close()
    return books

def update_book(book_id, title, author, published_date, isbn, page_count, cover, language):
    conn = get_db_connection()
    conn.execute('''
        UPDATE Books
        SET title = ?, author = ?, published_date = ?, isbn = ?, page_count = ?, cover = ?, language = ?
        WHERE id = ?
    ''', (title, author, published_date, isbn, page_count, cover, language, book_id))
    conn.commit()
    conn.close()

def delete_book(book_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM Books WHERE id = ?', (book_id,))
    conn.commit()
    conn.close()
