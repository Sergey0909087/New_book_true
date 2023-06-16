from django.db import models

class Blog(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    anons = models.CharField('Анонс', max_length=250)
    text = models.TextField('текст', max_length=250)
    src = models.CharField('Жанр', max_length=50)
# Create your models here.
