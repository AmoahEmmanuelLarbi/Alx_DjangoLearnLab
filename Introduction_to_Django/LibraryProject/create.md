# Documentation for inserting a data into a model using Django ORM

from bookshelf.models import Book
# Creating a Book instance
# Command
## book = Book(title="1984", author= "George Orwell", publication_year = 1949)
## book.save()
```
Book.objects.create(
    title = 'Atomic Habits',
    author = 'James Clear',
    publication_year = 1990
)
```
# RAW SQL
## INSERT INTO Book(title, author, publication_year) VALUES ("1948", "George Orwell",1949)

Book.objects.create(
    title = 'Test Book',
    author = 'Unknown',
    publication_year = 2000
)