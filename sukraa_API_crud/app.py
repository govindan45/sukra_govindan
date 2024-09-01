from flask import Flask, request, jsonify
from models import create_book, get_book, get_books, getAllBooks, update_book, delete_book
from database import init_db

app = Flask(__name__)


init_db()

@app.route('/books/Create', methods=['POST'])
def create_book_endpoint():
    data = request.json
    try:
        create_book(
            title=data['title'],
            author=data['author'],
            published_date=data['published_date'],
            isbn=data['isbn'],
            page_count=data.get('page_count'),
            cover=data.get('cover'),
            language=data.get('language')
        )
        return jsonify({'message': 'Book created successfully'}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book_endpoint(book_id):
    book = get_book(book_id)
    if book:
        book_By_Id = {
            "message":f"Book get By ID:{book_id}",
            "book":dict(book)
        }
        return jsonify(book_By_Id), 200
    else:
        return jsonify({'error': 'Book not found'}), 404

@app.route('/books/getBooks/', methods=['GET'])
def get_books_endpoint():
    filters = {
        'author': request.args.get('author'),
        'published_date': request.args.get('published_date'),
        'language': request.args.get('language')
    }
    books = get_books(filters)
    return jsonify([dict(book) for book in books]), 200

@app.route('/books/getAll/', methods=["GET"])
def get_All_Books():
    books = getAllBooks()
    return jsonify([dict(book) for book in books]), 200



@app.route('/books/update/<int:book_id>', methods=['PUT'])
def update_book_endpoint(book_id):
    data = request.json
    book = get_book(book_id)
    if book:
        update_book(
            book_id,
            title=data.get('title', book['title']),
            author=data.get('author', book['author']),
            published_date=data.get('published_date', book['published_date']),
            isbn=data.get('isbn', book['isbn']),
            page_count=data.get('page_count', book['page_count']),
            cover=data.get('cover', book['cover']),
            language=data.get('language', book['language'])
        )
        return jsonify({'message': 'Book updated successfully'}), 200
    else:
        return jsonify({'error': 'Book not found'}), 404

@app.route('/books/delete/<int:book_id>', methods=['DELETE'])
def delete_book_endpoint(book_id):
    book = get_book(book_id)
    if book:
        delete_book(book_id)
        return jsonify({'message': 'Book deleted successfully'}), 200
    else:
        return jsonify({'error': 'Book not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
