from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import FeedbackForm, MovieForm   

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

def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            print("=== Новое сообщение ===")
            print(f"Тема: {cleaned_data['subject']}")
            print(f"Email: {cleaned_data['email']}")
            print(f"Сообщение: {cleaned_data['text']}")
            print("========================")
            return redirect('home')
    else:
        form = FeedbackForm()
    
    return render(request, 'pages/contact.html', {'form': form})

def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm()
    return render(request, 'pages/movie_form.html', {'form': form, 'title': 'Добавить фильм'})

def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'pages/movie_form.html', {'form': form, 'title': 'Редактировать фильм'})