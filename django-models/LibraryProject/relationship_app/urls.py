# app-level urls
from django.urls import path, include
from .views import list_books, list_all_books, LibraryDetailView, LoginView
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", list_all_books),  # function-based view
    path("allbooks/", list_books.as_view()),
    path("library/<int:pk>", LibraryDetailView.as_view()),
    # new url to register, login and logout user
    path("register/", views.register.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("home/", views.index_page, name="home"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
