from django.db import models


class Scope(models.Model):
    topic = models.CharField(max_length=50, verbose_name='Тема')

    class Meta:
        verbose_name = 'Тематический раздел'
        verbose_name_plural = 'Тематические разделы'

    def __str__(self):
        return self.topic


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )
    scope = models.ManyToManyField('Scope', related_name='articles', through='ScopeRelation')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class ScopeRelation(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='tags')
    scope = models.ForeignKey('Scope', on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основной')

    def __str__(self):
        return '{} - {} '.format(self.article, self.scope)
