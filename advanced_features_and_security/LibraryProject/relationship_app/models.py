from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager

"""
Custom User Model
"""


# custom user manager
class CustomManager(BaseUserManager):
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
    profile_photo = models.ImageField(
        upload_to="profile_photos/", blank=True, null=True
    )

    # use custom manager
    objects = CustomManager()


# Create your models here.
# Author Model
class Author(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


# Book Model
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # reference Author

    def __str__(self):
        return f"{self.title} by {self.author.name}"

    class Meta:
        # custom permissions
        permissions = [
            ("can_add_book", "can add new book"),
            ("can_change_book", "can change new book"),
            ("can_delete_book", "can delete new book"),
        ]


# optimized query for ForeignKey
books = Book.objects.select_related("author").all()


# Library Model
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)  # reference book(many->many relationship)

    def __str__(self):
        return self.name


# optimized query for Many-Many
library_books = Library.objects.prefetch_related("books").all()


# Librarian Model
class Librarian(models.Model):
    name = models.CharField(max_length=100, null=False)
    library = models.OneToOneField(
        Library, on_delete=models.CASCADE
    )  # reference Library(one-> one relationship)


# Create a UserProfile model that includes a role field with predefined roles.
class UserProfile(models.Model):
    USER_ROLES = {
        "A": "Admin",
        "L": "Librarian",
        "M": "Member",
    }
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=1, choices=USER_ROLES)

    def __str__(self):
        return self.user
