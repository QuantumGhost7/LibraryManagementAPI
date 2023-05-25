# Library Management API
## Installation
1. Make sure you have Python and Django installed on your machine.
2. Clone the repository using the following command: 
  ```git clone <url> ```
3. Install the required dependencies by running the following command:
  ```pip install -r requirements.txt```
## Usage
1. Start the Django development server by running the following command:
  ```python manage.py runserver```
2. The API will be available at `http://localhost:8000/`.
3. You can interact with the API using an HTTP client (eg. Postman)

## API Endpoints
- **GET `/books/`**: Retrieve all books in the library.
- **GET `/books/<book_id>/`**: Retrieve a book by its ID.
- **POST `/books/create/`**: Create a new book by providing the necessary data in the request body.
- **PUT `/books/<book_id>/update/`**: Update a books information by specifying the book ID and providing the updated data in the request body.
- **DELETE `/books/<book_id>/delete/`**: Delete a book from the library by ID.

  

