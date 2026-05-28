from .models import Movie, Tag
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import FeedbackForm, MovieForm
from django.contrib import messages
from .forms import CommentForm

def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
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

@login_required
def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.author = request.user
            movie.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm()
    return render(request, 'pages/movie_form.html', {'form': form, 'title': 'Добавить фильм'})

@login_required
def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if movie.author != request.user:
        return redirect('home')  
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'pages/movie_form.html', {'form': form, 'title': 'Редактировать фильм'})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def movies_by_tag(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    movies = tag.movies.all()
    return render(request, 'pages/movies_by_tag.html', {'tag': tag, 'movies': movies})

@login_required
def add_comment(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.author = request.user
            comment.save()
            messages.success(request, 'Комментарий добавлен!')
        else:
            messages.error(request, 'Ошибка при добавлении комментария.')
    return redirect('movie_detail', pk=pk)
    from .forms import CommentForm

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    comment_form = CommentForm()
    return render(request, 'pages/movie_detail.html', {'movie': movie, 'comment_form': comment_form})
