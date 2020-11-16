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
        data = response.json()
        obj, _ = Place.objects.get_or_create(
            title=data['title'],
            description_short=data['description_short'],
            description_long=data['description_long'],
            longitude=data['coordinates']['lng'],
            latitude=data['coordinates']['lat'],
            defaults={},
        )
        for num, url in enumerate(data['imgs']):
            place_image = Image.objects.create(place_id=obj.id, number=num)
            r = requests.get(url)
            file_name = url.split('/')[-1]
            if r.status_code == requests.codes.ok:
                place_image.image.save(file_name, ContentFile(r.content))

        self.stdout.write(self.style.SUCCESS('Successfully upload place "{}"'.format(obj.title)))
