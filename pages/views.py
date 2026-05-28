from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import FeedbackForm

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