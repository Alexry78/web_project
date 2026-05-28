from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pages.views import (
    index, about, movie_detail, contact, movie_create, movie_update,
    register, movies_by_tag, add_comment
)

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('movie/<int:pk>/', movie_detail, name='movie_detail'),
    path('contact/', contact, name='contact'),
    path('movie/create/', movie_create, name='movie_create'),
    path('movie/<int:pk>/edit/', movie_update, name='movie_update'),
    path('accounts/register/', register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('tag/<int:tag_id>/', movies_by_tag, name='movies_by_tag'),
    path('movie/<int:pk>/comment/', add_comment, name='add_comment'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)