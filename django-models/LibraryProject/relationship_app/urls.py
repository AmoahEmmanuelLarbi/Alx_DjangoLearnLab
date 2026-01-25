# app-level urls
from django.urls import path
from .views import list_books, list_all_books, LibraryDetailView, LoginView
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", list_all_books),  # function-based view
    path("allbooks/", list_books.as_view()),
    path("library/<int:pk>", LibraryDetailView.as_view()),
    #new url to register, login and logout user
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout')
]
