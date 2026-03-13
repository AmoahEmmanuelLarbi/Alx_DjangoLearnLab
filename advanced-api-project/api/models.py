from django.db import models


# Create your models here.
# Author model
class Author(models.Model):
    name = models.CharField(max_length=50, null=False, verbose_name="Author name")


# Book model
class Book(models.Model):
    title = models.CharField(max_length=100, null=False, verbose_name="Title")
    publication_year = models.DateField(null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
