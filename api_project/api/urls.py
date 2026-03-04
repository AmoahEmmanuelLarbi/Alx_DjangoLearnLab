from django.urls import path
from .views import BookList

# urls(app-level)
urlpatterns = [
    path("books/", BookList.as_view(), name="book-list"),  # maps to the BookList View
]
