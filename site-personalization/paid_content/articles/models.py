from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    has_subscription = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Article(models.Model):
    title = models.CharField(max_length=128, verbose_name='Заголовок статьи')
    image = models.ImageField(verbose_name='Тематическое изображение', blank=True)
    text = models.TextField(verbose_name='Текст статьи')
    by_subscription = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title[:48]
