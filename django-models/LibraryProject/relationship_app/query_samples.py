from relationship_app.models import Author, Book, Library, Librarian

library_name = "Alx Library"
# list all books in the library
Book.objects.get(name=library_name)
Book.objects.all()

Book.objects.all().values()
author = Author.objects.create(name = "Kim Joe")
author_name = "James Smith"

# query all books by a specific author
Author.objects.get(name=author_name)
Author.objects.filter(author=author)
Book.objects.filter(author=author)
Author.objects.get(name=author_name)

Librarian.objects.all().values()


# ["Author.objects.get(name=author_name)", "objects.filter(author=author)"]