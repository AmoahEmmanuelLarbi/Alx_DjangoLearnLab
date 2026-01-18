from django.contrib import admin
from .models import Book
# Register your models here.

# implement custom configuration in the admin list view
class CustomBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title',)
    list_filter = ('author','publication_year')
    

admin.site.register(Book, CustomBookAdmin)