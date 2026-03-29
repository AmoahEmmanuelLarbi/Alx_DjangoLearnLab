from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic import (
    CreateView,
    TemplateView,
    UpdateView,
    ListView,
    DetailView,
    DeleteView,
)
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, ProfileEditForm, PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Post


# Create your views here.
def hellopage(request):

    return render(request, template_name="blog/login.html")


# creating view for new to signup
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")  # redirection page
    template_name = "account/register.html"


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
    template_name = "blog/post_list.html"
    queryset = Post.objects.all()

    # add extra context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["posts"] = self.get_queryset()
        context["total_posts"] = self.get_queryset().count()

        return context


# create a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostForm
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


# function-based view to allow only authenticated users to update their post
@login_required
def PostUpdateByOwner(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)  # get Post by pk

    # check if curretn user is the owner post
    # is_owner = request.user.is_authenticated and post.author == request.user
    # print(is_owner)

    if not post:
        return HttpResponseForbidden("Not allowed")

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        # validate data
        if form.is_valid():
            form.save()
            return redirect("posts")
    else:
        form = PostForm(instance=post)
    return render(
        request,
        "blog/post_create.html",
        {"form": form},
    )


# view to update post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/post_create.html"
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
    template_name = "blog/post_confirm_delete.html"
    context_object_name = "post"

    # only authors of post can edit the post
    def test_func(self):
        obj = self.get_object()
        print(obj)
        return obj.author == self.request.user
