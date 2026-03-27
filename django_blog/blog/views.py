from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (
    CreateView,
    TemplateView,
    UpdateView,
    ListView,
    DetailView,
    DeleteView,
)
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, ProfileEditForm, PostFrom
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from .models import Post


# Create your views here.
def hellopage(request):

    return render(request, template_name="blog/login.html")


# creating view for new to signup
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")  # redirection page
    template_name = "registration/signup.html"


# view for profile management
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "account/profile.html"


class ProfileEditView(LoginRequiredMixin, UpdateView):
    User = get_user_model()  # get current user model
    # model = User
    # fields = ["email"]
    form_class = ProfileEditForm
    template_name = "account/profile_edit.html"
    success_url = reverse_lazy("profile")

    def get_object(self):
        return self.request.user


# list all post
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list"
    queryset = Post.objects.all()

    # add extra context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["posts"] = self.get_queryset()
        context["total_posts"] = self.get_queryset().count()

        return context


# create a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostFrom
    template_name = "blog/post_create.html"
    success_url = reverse_lazy("posts")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid ❌")
        print(form.errors)
        return super().form_invalid(form)


# details view of each post
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"


# view to update post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/post_update.html"
    success_url = reverse_lazy("posts")

    # only authors of post can edit the post
    def test_func(self):
        obj = self.get_object()
        print(obj)
        return obj.author == self.request.user


# view to delete post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("posts")
    template_name = "blog/post_delete_confirm.html"
    context_object_name = "post"

    # only authors of post can edit the post
    def test_func(self):
        obj = self.get_object()
        print(obj)
        return obj.author == self.request.user
