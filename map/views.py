from django.shortcuts import render
from django.http import HttpResponse, Http404
from sightings.models import Sighting

# Create your views here.
def squirrel_map(request):
    if request:
        sightings = Sighting.objects.all()[:100]
        context = {
            'sightings': sightings
        }
        return render(request, 'map/map.html', context)
    else:
        Http404("Page Not Found")
