from django.urls import path, include
from .views import BookViewSet, BookList

# UserLoginApiView
from rest_framework.routers import DefaultRouter


# urls(app-level)
# create url using router(automatic URL routing)
router = DefaultRouter()
router.register(r"books_all", BookViewSet, basename="book_all")


urlpatterns = [
    # Include the router URLs for BookViewSet (all CRUD operations)
    path(
        "", include(router.urls)
    ),  # Include the router URLs for BookViewSet (all CRUD operations)
    # path("auth-login/", UserLoginApiView.as_view()),
    path("books/", BookList.as_view(), name="book-list"),  # maps to the BookList View
]
