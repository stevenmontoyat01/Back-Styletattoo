#Libraries
from django.conf.urls import include
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path("signUp/", views.signup.as_view(), name="signUp"),
    path("postUser/", views.postUser, name="postUser"),
    path("getUsers/", views.getUsers, name="getUser"),
    path("login/", views.Login.as_view(), name="login")
    
]