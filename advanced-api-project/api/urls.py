from django.urls import path
from .views import BookListView, BookDetailView, BookCreaeteView


urlpatterns = [
    path("books/", BookListView.as_view(), name="books"),
    path("book/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("create-book/", BookCreaeteView.as_view(), name="create-book"),
]
