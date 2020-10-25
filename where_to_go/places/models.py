from django.db import models

from django.db.models import JSONField


class Place(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description_short = models.CharField(max_length=500, verbose_name='Короткое описание')
    description_long = models.TextField(verbose_name='Полное описание')
    coordinates = JSONField(verbose_name='Координаты')

    def __str__(self):
        return self.title
