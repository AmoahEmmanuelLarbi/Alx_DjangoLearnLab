from django.db import models
from .models import Author, Book, Library

Book.objects.all()

author = Author.objects.create(name="Jones Acer")
book1 = Book.objects.create(title="System Design", author=author)
Book.objects.filter(author_id=1)

library = Library.objects.create(name="Alx Library")
library.books.add(book1)

Library.objects.all()
