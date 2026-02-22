from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .forms import ExampleForm
from django.views.generic.edit import FormView


# Create your views here.
# Create your views here.
@permission_required("bookshelf.can_view", raise_exception=True)
def list_all_books(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "bookshelf/book_list.html", context)


@permission_required("bookshelf.can_view", raise_exception=True)
def list_one_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "bookshelf/book_list.html", {"book": book})


def add_book(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("all-books")

    else:
        form = ExampleForm()
    return render(request, "bookshelf/form_example.html", {"form": form})
