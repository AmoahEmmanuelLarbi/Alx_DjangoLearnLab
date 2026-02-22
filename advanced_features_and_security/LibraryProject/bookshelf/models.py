from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
"""
Custom User Model
"""


# custom user manager
class CustomUserManager(BaseUserManager):
    # create a regular user
    def create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # create super user
    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, username, password, **extra_fields)


# custom user model
class CustomUser(AbstractUser):
    # new fields to add
    date_of_birth = models.DateField(null=False, verbose_name="date of birth")
    # profile_photo = models.ImageField(
    #     upload_to="profile_photos/", blank=True, null=True
    # )
    email = models.EmailField(unique=True)

    # use custom manager
    objects = CustomUserManager()


class Book(models.Model):
    # ROLE_CHOICES = (
    #     ("admin", "Admin"),
    #     ("editor", "Editor"),
    #     ("viewer", "Viewer"),
    # )

    # role = models.CharField(
    #     max_length=10,
    #     choices=ROLE_CHOICES,
    #     default="viewer",
    # )

    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    author_name = models.CharField(max_length=50, blank=False, null=False)
    publication_date = models.DateField(null=True)

    class Meta:
        permissions = [
            ("can_view", "can view a book"),
            ("can_create", "can create a book"),
            ("can_edit", "can edit a book"),
            ("can_delete", "can delete a book"),
        ]
