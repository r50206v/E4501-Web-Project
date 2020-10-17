import os
import sys
import inspect
from django.shortcuts import render
from sightings.models import Sighting


# Create your views here.
def index(request):
    squ = Sighting.objects.all()
    sightings = squ[:100]
    context = {
        'sightings': sightings
    }
    pass
