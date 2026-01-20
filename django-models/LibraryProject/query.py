# Book.objects.all()
# """
# <QuerySet [<Book: Introduction to DSA by James Smith>, <Book: Python for beginners by James Smith>, <Book: System Design by James Smith>]>
# """


# author = Author.objects.create(name="Jones Acer")
# book1 = Book.objects.create(title="System Design", author=author)
# Book.objects.filter(author_id=1)
# Book.objects.filter(author__name = author)
# Book.objects.filter(author = author)

# library = Library.objects.create(name="Alx Library")
# library.books.add(book1)

# author_name = "James Smith"
# #query allbooks by a specific author
# Author.objects.get(name = author_name)
# Author.objects.filter(author = author)
# Library.objects.all()

# get_library = Library.objects.filter(name = "Alx Library")
# #get librarian for a library
# Librarian.objects.filter(library = get_library)


# def query_all_books_by_author():
#     """
#     Docstring for query_all_books_by_author
#     Query all books by a specific autor
#     """
#     return Book.objects.filter(author_id = 1)

# from relationship_app.models import Book, Library, Librarian


# # Query 1: Query all books by a specific author
# def get_books_by_author(author_name):
#     """
#     Returns all books written by a specific author.
#     """
#     return Book.objects.filter(author__iexact=author_name)


# # Query 2: List all books in a library
# def get_books_in_library(library_name):
#     """
#     Returns all books available in a specific library.
#     """
#     library = Library.objects.get(name=library_name)
#     return library.books.all()


# # Query 3: Retrieve the librarian for a library
# def get_librarian_for_library(library_name):
#     """
#     Returns the librarian responsible for a specific library.
#     """
#     library = Library.objects.get(name=library_name)
#     return library.librarian

# from relationship_app.models import Author, Book, Library


# def query_books_by_author(author_name):
#     """
#     Query all books by a specific author.
#     """
#     author = Author.objects.get(name=author_name)
#     return Book.objects.filter(author=author)


# def list_books_in_library(library_name):
#     """
#     List all books in a library.
#     """
#     library = Library.objects.get(name=library_name)
#     return library.books.all()


# def get_library_librarian(library_name):
#     """
#     Retrieve the librarian for a library.
#     """
#     library = Library.objects.get(name=library_name)
#     return library.librarian

# def get_books_by_author(author_name):
#     Author.objects.get(name=author_name)
#     return objects.filter(author=author)