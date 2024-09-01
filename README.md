This project is a simple  API built using  that interacts with an SQLite3 database to perform CRUD (Create, Read, Update, Delete) operations on a dataset of books.

## Project Overview

The Book API allows users to manage a collection of books by providing functionalities to create, read, update, and delete book records stored in an SQLite3 database. The API is built using the FastAPI framework, which provides high performance and easy-to-use features for building modern web APIs.

## Features

- **Create a Book**: Add a new book to the database.
- **Get Book by ID**: Retrieve a specific book's details using its ID.
- **Get Books with Filters**: List books with optional filters for author, published date, and language.
- **Update a Book**: Modify the details of an existing book.
- **Delete a Book**: Remove a book from the database by its ID.
- **Error Handling**: Proper error handling for invalid data and operations.

## Requirements

- Python 3.8+
- FlaskAPI
- sqlite3


## Running the Application

1. **Initialize the database:**

    Run the following command to create the SQLite database and tables:

    ```
    python -c "from app.database import create_db; create_db()"
    ```



2. **Access the API documentation:**

    Open your browser and go to `http://127.0.0.1:8000/docs` to view the automatically generated API documentation using Swagger UI.

## API Endpoints

1. **Create a Book**: `POST /books/`

    - Request Body: JSON object containing book details.
    - Example:
      ```json
      {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "published_date": "1925-04-10",
        "isbn": "9780743273565",
        "page_count": 180,
        "cover": "http://example.com/gatsby.jpg",
        "language": "English"
      }
      ```

2. **Get Book by ID**: `GET /books/{id}`

    - Response: JSON object of the book's details or 404 if not found.

3. **Get Books with Filters**: `GET /books/`

    - Query Parameters: `author`, `published_date`, `language` (all optional).
    - Example: `/books?author=Fitzgerald&language=English`

4. **Update a Book**: `PUT /books/{id}`

    - Request Body: JSON object with the updated book details.
    - Example:
      ```json
      {
        "title": "The Great Gatsby - Updated"
      }
      ```

5. **Delete a Book**: `DELETE /books/{id}`

    - Response: JSON object of the deleted book's details or 404 if not found.



