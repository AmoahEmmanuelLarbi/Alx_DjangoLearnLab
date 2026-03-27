from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager


# Create your models here.
# create CustomUser Manager
# class CustomManager(BaseUserManager):
#     def create_user(self, username, password):
#         """
#         Create and save a user with the given email and password.
#         """
#         if not username:
#             raise ValueError("Username is requried !")
#         user = self.model(username=username)
#         user.set_password(password)
#         user.save(using=self.db)
#         return user


# custom user model
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)

    # modify: add extra fields

    def __str__(self):
        return self.email


# blog model
class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
