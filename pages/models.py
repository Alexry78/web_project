from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название фильма")
    director = models.CharField(max_length=200, verbose_name="Режиссёр", blank=True)
    description = models.TextField(verbose_name="Описание", blank=True)
    release_year = models.IntegerField(verbose_name="Год выпуска", null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Рейтинг", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    is_showing = models.BooleanField(default=True, verbose_name="Сейчас в прокате")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"