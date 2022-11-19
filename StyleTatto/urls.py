from django.contrib import admin
from django.urls import path,include
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include('accounts.urls')),
    path("tattos/", include('tatto.urls')),
    path("porta/", include('Portafolio.urls'))


]
