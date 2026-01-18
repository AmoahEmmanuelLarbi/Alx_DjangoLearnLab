from django.db import models
from .models import Book

Book.objects.all()
Book.objects.filter(author_id = 1)