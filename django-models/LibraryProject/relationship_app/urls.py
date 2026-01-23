# app-level urls
from django.urls import path
from .views import list_books, list_all_books, LibraryDetailView

urlpatterns = [
    path("", list_all_books),  # function-based view
    path("allbooks/", list_books.as_view()),
    path("library/<int:pk>", LibraryDetailView.as_view()),
]
