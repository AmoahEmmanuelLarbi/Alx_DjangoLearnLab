from relationship_app.models import Author, Book, Library, Librarian


Book.objects.all().values()
author = Author.objects.create(name = "Kim Joe")
author_name = "James Smith"

Author.objects.get(name=author_name)
Book.objects.filter(author=author)
Author.objects.get(name=author_name)
objects.filter(author=author)