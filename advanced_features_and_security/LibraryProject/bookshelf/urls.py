from django.urls import path
from . import views

urlpatterns = [
    path("all-books/", views.list_all_books),
    path("book/<int:pk>/", views.list_one_book),
]
