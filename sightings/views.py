from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from .models import Sighting
from .form import SquirrelForm


# Create your views here.
def squirrel_id(request, unique_squirrel_id):
    pass


def add(request):
    pass

def stats(request):
    pass

def all_squirrels(request):
    pass