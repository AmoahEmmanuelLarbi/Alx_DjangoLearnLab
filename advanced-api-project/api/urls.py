from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookDeleteView,
    BookUpdateView,
)


urlpatterns = [
    path("books/", BookListView.as_view(), name="books"),
    path("book/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("books/update/<int:pk>/", BookUpdateView.as_view(), name="book-update"),
    path("books/create/", BookCreateView.as_view(), name="create-book"),
    path("books/delete/<int:pk>/", BookDeleteView.as_view()),
]
