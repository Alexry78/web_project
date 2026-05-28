from django.contrib import admin
from django.urls import path
from pages.views import index, about

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),
]