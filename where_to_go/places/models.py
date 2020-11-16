from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    short_description = models.TextField(verbose_name='Короткое описание', blank=True)
    long_description = HTMLField(verbose_name='Полное описание', blank=True)
    longitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(verbose_name='Картинка')
    place = models.ForeignKey('Place', on_delete=models.CASCADE, related_name='images', verbose_name='Место')
    number = models.PositiveIntegerField(default=0, verbose_name='Позиция')

    class Meta:
        ordering = ['number', ]

    def __str__(self):
        return '{} {}'.format(self.number, self.place.title)
