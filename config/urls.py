from django.contrib import admin
from django.urls import path
from pages.views import index, about, movie_detail   
from django.conf import settings
from django.conf.urls.static import static
from pages.views import index, about, movie_detail, contact

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('movie/<int:pk>/', movie_detail, name='movie_detail'), 
    path('contact/', contact, name='contact'),  
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)