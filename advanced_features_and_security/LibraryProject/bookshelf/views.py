from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import HttpResponse


# Create your views here.
# Create your views here.
def list_all_books(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "bookshelf/index.html", context)


def list_one_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "bookshelf/index.html", {"book": book})
