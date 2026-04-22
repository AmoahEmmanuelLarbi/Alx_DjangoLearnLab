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
from .forms import SignUpForm, ProfileEditForm, PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Post, Comment
from django.db.models import Q
from taggit.models import Tag

# implement pagination
from django.core.paginator import Paginator


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

    def get_queryset(self):
        queryset = Post.objects.all()

        # Implement a search feature that allows users to search for posts based on the title, content, or tags.
        title = self.request.GET.get("title")
        author = self.request.GET.get("author")
        content = self.request.GET.get("content")
        # print(f"Username: {author}")

        if author:
            queryset = queryset.filter(author__username=author)
        if title:
            queryset = queryset.filter(title__startswith="A")

        return queryset

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

    # if not post:
    #     return HttpResponseForbidden("Not allowed")

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


# views to handle CRUC operations for comments
@login_required
def post_comments(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)

    context = {"post": post, "comments": comments}

    return render(request, "comment/comment_list.html", context)


# create view for comments
@login_required
def create_comment(request, pk):
    # first get a post
    post = get_object_or_404(Post, pk=pk)

    # create a comment
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect("posts")

    else:
        form = CommentForm()

    return render(request, "comment/comment_form.html", {"form": form, "post": post})


# view to create a new comment
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "comment/comment_form.html"

    def form_valid(self, form):
        # comment = form.save(commit=False)
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs["pk"])
        return super().form_valid(form)


# update view for comment
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "comment/comment_form.html"
    # success_url = reverse_lazy('comments')

    # only authors of comment can edit the comment
    def test_func(self):
        obj = self.get_object()
        print(obj)
        return obj.author == self.request.user

    def get_success_url(self):
        print(self.object.post.pk)
        return reverse_lazy("comments", kwargs={"pk": self.object.post.pk})


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = "comment/comment_confirm_delete.html"
    context_object_name = "comment"

    # only authors of comment can delete the post
    def test_func(self):
        obj = self.get_object()
        print(obj)
        return obj.author == self.request.user

    # success url
    def get_success_url(self):
        print(f"Post pk:{self.object.post.pk}")
        return reverse_lazy("comments", kwargs={"pk": self.object.post.pk})


# function based view to show all post
def show_all_post(request):
    posts = Post.objects.all()

    title = request.GET.get("query")
    # author = request.GET.get("author")
    content = request.GET.get("query")
    tags = request.GET.get("query")
    # print(f"Username: {author}")

    # if author:
    #     posts = posts.filter(author__username=author)
    if title or content:
        posts = posts.filter(
            Q(title__icontains=title)
            | Q(content__icontains=content)
            | Q(tags__name__icontains=tags)
        ).distinct()

    paginator = Paginator(object_list=posts, per_page=5)
    print(paginator.num_pages)
    total_obj = paginator.count
    number_of_obj_per_page = paginator.num_pages
    page_range = paginator.page_range
    # page_obj = paginator.get_page(6)
    page_num = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_num)
    page_number = page_obj.number

    context = {
        "posts": page_obj,
        "total_obj": total_obj,
        "number_of_obj": number_of_obj_per_page,
        "page_range": page_range,
        "page_number": page_number,
    }

    return render(request, "blog/post_list.html", context)


# view to show tagged post
class TagView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 10
    template_name = "blog/tag_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        print(f"Kwargs: {self.kwargs}")
        self.tag_name = self.kwargs.get("tag_name")
        # tag_slug = self.kwargs.get("tag_slug")
        print(f"Tag slug: {self.kwargs.get('tag_slug')}")
        # queryset = Post.objects.filter(tags__name__iexact=tag_name).distinct()
        queryset = Post.objects.filter(tags__name__iexact=self.tag_name).distinct()
        print(queryset.query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context["tag_slug"] = self.kwargs.get("tag_slug")
        # tag_slug = self.kwargs.get('tag_slug')
        # tag_name = self.kwargs.get("tag_name")
        context["tag"] = get_object_or_404(Tag, slug__iexact=self.tag_name)
        return context

class PostByTagListView(LoginRequiredMixin ,ListView):
    model = Post
    paginate_by = 10
    template_name = "blog/tag_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        self.tag_slug = self.kwargs.get('tag_slug')
        queryset = Post.objects.filter(tags__slug__iexact=self.tag_slug).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['tag'] = get_object_or_404(Tag, slug__iexact=self.tag_slug)
        return context