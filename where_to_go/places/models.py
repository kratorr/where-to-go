from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description_short = models.CharField(max_length=500, verbose_name='Короткое описание')
    description_long = models.TextField(verbose_name='Полное описание')
    coordinates = models.JSONField(verbose_name='Координаты')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField()
    place = models.ForeignKey('Place', on_delete=models.CASCADE, related_name='images')
    number = models.PositiveIntegerField(null=False)

    class Meta:
        unique_together = (('place', 'number'),)

    def __str__(self):
        return '{} {}'.format(self.number, self.place.title)
