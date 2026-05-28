from django.db import models
from django.contrib.auth.models import User 

class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название фильма")
    director = models.CharField(max_length=200, verbose_name="Режиссёр", blank=True)
    description = models.TextField(verbose_name="Описание", blank=True)
    release_year = models.IntegerField(verbose_name="Год выпуска", null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Рейтинг", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    is_showing = models.BooleanField(default=True, verbose_name="Сейчас в прокате")
    image = models.ImageField(upload_to='movies/', verbose_name="Постер", blank=True, null=True)  
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"