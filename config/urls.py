from django.contrib import admin
from django.urls import path
from pages.views import index

urlpatterns = [
    path('', index, name='home'),
    path('admin/', admin.site.urls),
]