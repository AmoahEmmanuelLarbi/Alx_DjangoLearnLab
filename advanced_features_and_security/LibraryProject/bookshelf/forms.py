from django import forms
from django.contrib.auth.forms import (
    UserChangeForm,
    UserCreationForm,
)
from .models import CustomUser, Book


# custom_creation_form
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "date_of_birth")


# custom_change_form
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            "title",
            "description",
            "author_name",
            "publication_date",
        )
        