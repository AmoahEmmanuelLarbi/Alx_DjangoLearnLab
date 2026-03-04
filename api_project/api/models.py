from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50, null=False, verbose_name="Title")
    author = models.CharField(max_length=50, null=True, verbose_name="Author")
