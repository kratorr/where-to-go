import requests

from urllib.parse import  urlparse
from pathlib import Path

from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Upload place data from json to DB'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str)

    def handle(self, *args, **options):
        response = requests.get(options['url'])
        response.raise_for_status()
        place_data = response.json()
        place, is_created = Place.objects.update_or_create(
            title=place_data['title'],
            defaults={
                'short_description': place_data['description_short'],
                'long_description': place_data['description_long'],
                'longitude': place_data['coordinates']['lng'],
                'latitude': place_data['coordinates']['lat']
            }
        )

        if not is_created:
            place.images.all().delete()

        for num, url in enumerate(place_data['imgs']):
            place_image = Image.objects.create(place_id=place.id, number=num)
            request = requests.get(url)
            file_name = Path(urlparse(url).path).name
            request.raise_for_status()
            place_image.image.save(file_name, ContentFile(request.content))

        self.stdout.write(self.style.SUCCESS('Successfully upload place "{}"'.format(place.title)))
