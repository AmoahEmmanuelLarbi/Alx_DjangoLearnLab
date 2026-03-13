from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .models import Book, Author
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter


# Create your views here.
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# using generic views
class BookListView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        title = self.request.query_params.get("title")
        author = self.request.query_params.get("author")
        publication_year = self.request.query_params.get("publication_year")

        if title:
            return Book.objects.filter(title__icontains=title)

        if author:
            return Book.objects.filter(author__iexact=author)

        if publication_year:
            return Book.objects.filter(publication_year=publication_year)
        return Book.objects.all()

    # implement search functionality
    filter_backends = [SearchFilter]
    search_fields = ["title"]


class BookDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # logged-in user is the automatic of the book created
    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class BookUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
