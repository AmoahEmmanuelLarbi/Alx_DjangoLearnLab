from relationship_app.models import Author, Book, Library, Librarian


Book.objects.all().values()
author_name = "James Smith"
Author.objects.get(name= author_name)
# Author.objects.filter(author = author)