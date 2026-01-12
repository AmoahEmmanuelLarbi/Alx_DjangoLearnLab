from django.urls import path
from . import views

#mandatory in urls
urlpatterns = [
    path("", views.home, name="home"),
    path("hello/", views.welcome)
    # path("home/", views.home, name="home")
]