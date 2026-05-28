from django.shortcuts import render
from .models import Movie   

def index(request):
    movies = Movie.objects.all()  
    return render(request, 'pages/index.html', {'movies': movies})

def about(request):
    return render(request, 'pages/about.html')