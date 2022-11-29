from django.urls import path
from quotes import views
from . import views
from .views import *

urlpatterns = [
    path('', views.ViewsQuotes.as_view(), name="quotes"),
    path('deleteQuotes/<int:id>',views.DeleteQuotes.as_view(), name="quotes_process"),
    path('updateQuote/<int:id>',views.UpdateQuotes.as_view(), name="quotes_process")
]
