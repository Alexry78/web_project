from django.shortcuts import render
from .models import Movie

def index(request):
    movies = Movie.objects.all()  
    context = {
        'movies': movies
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')