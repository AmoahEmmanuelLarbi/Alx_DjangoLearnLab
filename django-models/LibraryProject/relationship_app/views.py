from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic import ListView
from django.views.generic.detail import DetailView


# Create your views here.
# function-based view that lists all books store in the database
def list_all_books(request):
    books = Book.objects.all()  # retrieve all books
    context = {"books": books}
    return render(request, "relationship_app/list_books.html", context)


# implement class-based view
"""Create a class-based view in relationship_app/views.py 
that displays details for a specific library, 
listing all books available in that library.
"""


class list_book(ListView):
    model = Book
    template_name = "relationship_app/library_detail.html"

    def get_queryset(self):
        # return Book.objects.all()
        library = Library.objects.get(name__iexact="Alx Library")
        all_books = library.books.all()
        return all_books

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["library"] = Library.objects.get(name__iexact="Alx Library")
        context["library_books"] = context["object_list"].values()
        return context


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/demo.html"

    def get_queryset(self):
        library = Library.objects.get(self, )
