from . import views
from django.urls import path



urlpatterns = [
     path("signup/", views.signUpView.as_view(), name="signup" ),
     path("login/", views.Login.as_view(),name="login")
]