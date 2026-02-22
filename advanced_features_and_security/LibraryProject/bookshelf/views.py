from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required


# Create your views here.
# Create your views here.
@permission_required("book_list.can_view", raise_exception=True)
def list_all_books(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "bookshelf/index.html", context)


@permission_required("bookshelf.can_view", raise_exception=True)
def list_one_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "bookshelf/index.html", {"book": book})
