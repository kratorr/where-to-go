from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description_short = models.CharField(max_length=500, verbose_name='Короткое описание')
    description_long = HTMLField(verbose_name='Полное описание')
    longitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(verbose_name='Картинка')
    place = models.ForeignKey('Place', on_delete=models.CASCADE, related_name='images')
    number = models.PositiveIntegerField(default=0, null=False, verbose_name='Позиция')

    class Meta:
        ordering = ['number', ]

    def __str__(self):
        return '{} {}'.format(self.number, self.place.title)
