from django.shortcuts import render
from .models import Book

# Create your views here.
# function-based view that lists all books store in the database
def list_all_books(request):
    books = Book.objects.all() #retrieve all books
    context = {'books': books}
    return render(request, 'list_books.html', context)
