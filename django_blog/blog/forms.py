from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Post, Comment

# create SignUp form
User = get_user_model()


# user registration form
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")


# form to edit your profile
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "email",
            "username",
        )

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if email:
            # normalize email
            email = email.strip().lower()

            # check if email already exists (excluding current user)
            if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError("This email is already taken")

        return email


# post creation form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "content",
        )

    def clean_title(self):
        title = self.cleaned_data.get("title")

        # clean title
        if title:
            title = title.strip()

        # check if title length of characters is less than 10
        if len(title) < 10:
            raise forms.ValidationError("Title of post cannot less than 10 characters")

        return title


# comment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)

    def clean_content(self):
        content = self.cleaned_data.get("content")
        # check if not content (comment is provided)
        if not content:
            raise forms.ValidationError("Comment content must be provided")
        return content
