from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'director', 'description', 'release_year', 'rating', 'is_showing', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'director': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'release_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'is_showing': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Название фильма',
            'director': 'Режиссёр',
            'description': 'Описание',
            'release_year': 'Год выпуска',
            'rating': 'Рейтинг (0–10)',
            'is_showing': 'Сейчас в прокате',
            'image': 'Постер',
        }

class FeedbackForm(forms.Form):
    subject = forms.CharField(
        label='Тема',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    text = forms.CharField(
        label='Сообщение',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
    )