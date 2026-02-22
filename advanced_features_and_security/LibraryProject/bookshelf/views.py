from django.shortcuts import render
from .models import Book

# Create your views here.
# Create your views here.
def list_all_books(request):
    books = Book.objects.all()
    context = {"books": books}