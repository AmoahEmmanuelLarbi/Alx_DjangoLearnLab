from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .models import Book, Author
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# using generic views
class BookListView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # implement search functionality
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = ["title"]
    ordering_fields = ["publication_year"]
    search_fields = ["title"]

    # def get_queryset(self):
    #     title = self.request.query_params.get("title")
    #     author = self.request.query_params.get("author")
    #     publication_year = self.request.query_params.get("publication_year")

    #     if title:
    #         return Book.objects.filter(title__icontains=title)

    #     if author:
    #         return Book.objects.filter(author__iexact=author)

    #     if publication_year:
    #         return Book.objects.filter(publication_year=publication_year)
    #     return Book.objects.all()

    # implement search functionality
    # filter_backends = [SearchFilter]
    # search_fields = ["title"]


class BookDetailView(generics.RetrieveAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # logged-in user is the automatic of the book created
    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class BookUpdateView(generics.UpdateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDeleteView(generics.DestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
