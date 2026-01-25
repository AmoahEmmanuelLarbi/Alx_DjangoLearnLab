# app-level urls
from django.urls import path
from .views import list_books, list_all_books, LibraryDetailView, RegisterView, LoginView

urlpatterns = [
    path("", list_all_books),  # function-based view
    path("allbooks/", list_books.as_view()),
    path("library/<int:pk>", LibraryDetailView.as_view()),
    #new url to register, login and logout user
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout')
]
