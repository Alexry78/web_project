from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Movie

def index(request):
    movies = Movie.objects.all()  
    context = {
        'movies': movies
    }
    return render(request, 'pages/index.html', context)

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)   
    return render(request, 'pages/movie_detail.html', {'movie': movie})


def about(request):
    return render(request, 'pages/about.html')