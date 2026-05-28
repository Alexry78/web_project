from django.shortcuts import render

def index(request):
    context = {
        'welcome_text': 'Добро пожаловать в наш сервис!',
        'books': [
            {'title': 'Книга 1', 'description': 'Описание первой книги'},
            {'title': 'Книга 2', 'description': 'Описание второй книги'},
            {'title': 'Книга 3', 'description': 'Описание третьей книги'},
        ]
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')