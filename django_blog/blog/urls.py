from django.urls import reverse_lazy
from django.urls import path
from .views import hellopage
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_view
from .views import (
    SignUpView,
    ProfileView,
    ProfileEditView,
    PostCreateView,
    PostListView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    PostUpdateByOwner,
    post_comments,
    create_comment,
    CommentUpdateView,
    CommentDeleteView,
    show_all_post,
)


urlpatterns = [
    # path("", hellopage, name="hello"),
    path("home/", TemplateView.as_view(template_name="blog/home.html"), name="home"),
    # urls for profile management
    # user signup
    path("register/", SignUpView.as_view(), name="register"),
    # user login and logout
    path(
        "login/",
        auth_view.LoginView.as_view(template_name="blog/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_view.LogoutView.as_view(template_name="blog/logout.html"),
        name="logout",
    ),
    # user profile management
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/edit/", ProfileEditView.as_view(), name="profile-edit"),
    # password change
    path(
        "password_change/",
        auth_view.PasswordChangeView.as_view(
            template_name="account/password_change_form.html",
            success_url=reverse_lazy("password_change_done"),
        ),
        name="password_change",
    ),
    path(
        "password_change/done/",
        auth_view.PasswordChangeDoneView.as_view(
            template_name="account/password_change_done.html"
        ),
        name="password_change_done",
    ),
    # password reset
    path(
        "password_reset/",
        auth_view.PasswordResetView.as_view(
            template_name="account/password_reset_form.html",
            success_url=reverse_lazy("password_reset_done"),
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_view.PasswordResetDoneView.as_view(
            template_name="account/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_view.PasswordResetConfirmView.as_view(
            template_name="account/password_reset_confirm.html",
            success_url=reverse_lazy("password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_view.PasswordResetCompleteView.as_view(
            template_name="account/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    # post CRUD urls
    path("posts/", show_all_post, name="posts"),
    path("post/new/", PostCreateView.as_view(), name="create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateByOwner, name="post-edit"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    # comment CRUD urls
    path("posts/<int:pk>/comments/new/", post_comments, name="comments"),
    path("comment/<int:pk>/new/", create_comment, name="create-comment"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment-edit"),
    path(
        "comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"
    ),
]
