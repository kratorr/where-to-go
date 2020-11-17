from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Place


def get_places(request):
    places = Place.objects.all()
    place_data = {"type": "FeatureCollection", "features": []}
    for place in places:
        place_data['features'].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.longitude, place.latitude]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse('get_place', args=[place.id])
                }
            }
        )
    return render(request, 'index.html', context={'data': place_data})


def get_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    data = {
        "title": place.title,
        "imgs": [request.build_absolute_uri(image.image.url) for image in place.images.all()],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude
        }
    }
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False, 'indent': 4})
