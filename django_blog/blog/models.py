from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager
from taggit.managers import TaggableManager


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


# tag model
# class Tag(models.Model):
#     name = models.CharField(max_length=50, unique=True, blank=False)

#     def __str__(self):
#         return f"Tag name: {self.name}"


# blog model
class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # tags = models.ManyToManyField(Tag, related_name='posts')  # many-to-many relationship
    # add tag
    tags = TaggableManager()

    def __str__(self):
        return f"Post: {self.title}"


"""
In this task, you will expand the django_blog project by adding a comment feature to the blog posts. 
Users will be able to read comments, and authenticated users will have the ability to post, edit, and delete their comments.
"""


# comment model
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # that records the time the comment was made.
    updated_at = models.DateTimeField(
        auto_now=True
    )  # that records the last time the comment was updated.

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"
