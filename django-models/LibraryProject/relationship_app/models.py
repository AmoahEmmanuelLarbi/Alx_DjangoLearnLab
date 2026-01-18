from django.db import models


# Create your models here.
# Author Model
class Author(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


# Book Model
class Book(models.Model):
    title = models.CharField(max_length=100, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # reference Author

    def __str__(self):
        return f"{self.title} by {self.author.name}"


# Library Model
class Library(models.Model):
    name = models.CharField(max_length=100, null=False)
    books = models.ManyToManyField(Book)  # reference book(many->many relationship)

    def __str__(self):
        return f"{self.name} {len(self.books)} books"

# Librarian Model
class Librarian(models.Model):
    name = models.CharField(max_length=100, null=False)
    library = models.OneToOneField(Library, on_delete=models.CASCADE) #reference Library(one-> one relationship)