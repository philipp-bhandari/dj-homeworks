from django.db import models


class Scope(models.Model):
    topic = models.CharField(max_length=32, verbose_name='раздел')

    class Meta:
        verbose_name = 'раздел'
        verbose_name_plural = 'разделы'

    def __str__(self):
        return self.topic


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='название')
    text = models.TextField(verbose_name='текст')
    published_at = models.DateTimeField(verbose_name='дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='изображение', )
    scopes = models.ManyToManyField(Scope, through='ArticleScope')

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'

    def __str__(self):
        return self.title


class ArticleScope(models.Model):
    scopes = models.ForeignKey(Scope, on_delete=models.CASCADE, verbose_name='теги')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='основной')

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return 'раздел'
