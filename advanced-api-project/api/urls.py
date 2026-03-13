from django.urls import path
from .views import ListView, DetailView, CreateView, DeleteView, UpdateView


urlpatterns = [
    path("books/", ListView.as_view(), name="books"),
    path("book/<int:pk>/", DetailView.as_view(), name="book-detail"),
    path("books/update/<int:pk>/", UpdateView.as_view(), name="book-update"),
    path("books/create/", CreateView.as_view(), name="create-book"),
    path("books/delete/<int:pk>/", DeleteView.as_view()),
]
