from . import views
from django.urls import path



urlpatterns = [
     path("signup/", views.signUpView.as_view(), name="signup" ),
]