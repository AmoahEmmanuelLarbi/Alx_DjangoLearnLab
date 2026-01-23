# app-level urls
from django.urls import path
from .views import list_book, list_all_books, LibraryDetailView

urlpatterns = [
    path("", list_all_books),  # function-based view
    path("allbooks/", list_book.as_view()),
    path("library/<int:pk>", LibraryDetailView.as_view()),
]
