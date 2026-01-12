# Documentation of 
from bookshelf.models import Book

book = Book.objects.all()[0]
book.title = "Nineteen Eighty-Four"
book.save()