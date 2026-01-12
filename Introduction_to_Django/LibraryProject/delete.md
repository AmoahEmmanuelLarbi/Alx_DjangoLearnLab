# Documentation to delete a book
from bookshelf.models import Book
book = Book.objects.all()[2]

book.delete()