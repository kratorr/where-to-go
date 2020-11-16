import requests

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
        place, _ = Place.objects.get_or_create(
            title=place_data['title'],
            description_short=place_data['description_short'],
            description_long=place_data['description_long'],
            longitude=place_data['coordinates']['lng'],
            latitude=place_data['coordinates']['lat'],
            defaults={},
        )
        for num, url in enumerate(place_data['imgs']):
            place_image = Image.objects.create(place_id=place.id, number=num)
            request = requests.get(url)
            file_name = url.split('/')[-1]
            request.raise_for_status()
            place_image.image.save(file_name, ContentFile(request.content))

        self.stdout.write(self.style.SUCCESS('Successfully upload place "{}"'.format(place.title)))
