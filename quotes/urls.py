from django.urls import path
from quotes import views
from . import views
from .views import QuotesView

urlpatterns = [
    path('quotes/', views.QuotesView.as_view(), name="quotes"),
    path('quotes/<int:id>', views.QuotesView.as_view(), name="quotes_process"),
]
