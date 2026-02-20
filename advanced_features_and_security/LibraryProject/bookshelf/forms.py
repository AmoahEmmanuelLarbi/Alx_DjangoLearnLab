from django.contrib.auth.forms import (
    UserChangeForm,
    UserCreationForm,
)
from .models import CustomUser


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
