from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'release_year', 'rating', 'is_showing', 'created_at')
    list_filter = ('is_showing', 'release_year')
    search_fields = ('title', 'director')