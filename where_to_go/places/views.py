from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse

from .models import Place


def index(request):
    places = Place.objects.all()
    data = {"type": "FeatureCollection", "features": []}
    for place in places:
        data['features'].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.longitude, place.latitude]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse('place_retrive', args=[place.id])
                }
            }
        )

    template = loader.get_template('index.html')
    context = {'data': data}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def place_retrive(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    data = {
        "title": place.title,
        "imgs": [request.build_absolute_uri(image.image.url) for image in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude
        }
    }
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False, 'indent': 4})
