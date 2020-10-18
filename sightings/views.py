from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from .models import Sighting
from .form import SquirrelForm


# Create your views here.
def squirrel_id(request, unique_squirrel_id):
    if not request: 
        return Http404("Page Not Found")

    data = Sighting.objects.filter(unique_squirrel_id=unique_squirrel_id).first()
    if request.method == "POST":
        form = SquirrelForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/sightings')
    else:
        form = SquirrelForm(instance=data)
        context = {'form': form}
        return render(request, 'sightings/update.html', context)


def add(request):
    if not request: 
        return Http404("Page Not Found")

    if request.method == "POST":
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sightings')
    else:
        form = SquirrelForm()
        context = {'form': form}
        return render(request, 'sightings/add.html', context)


def stats(request):
    if request:
        numSquirrels = Sighting.objects.values('unique_squirrel_id').distinct().count()
        numSites = Sighting.objects.all().count()
        amFreq = Sighting.objects.filter(shift="AM").count()
        pmFreq = Sighting.objects.filter(shift="PM").count()
        adultRatio = Sighting.objects.filter(age='Adult').values('unique_squirrel_id').distinct().count()
        juvenileRatio = Sighting.objects.filter(age='Juvenile').values('unique_squirrel_id').distinct().count()
        adultRatio = adultRatio / numSquirrels
        juvenileRatio = juvenileRatio / numSquirrels

        context = {
            "number of unique squirrels": numSquirrels,
            "number of sites": numSquirrels,
            "frequency of seeing squirrels in AM time": amFreq,
            "frequency of seeing squirrels in PM time": pmFreq,
            "ratio of adult squirrels": adultRatio,
            "ratio of juvenile squirrels": juvenileRatio
        }
        return render(request, "sightings/stats.html", {"context": context})
    else:
        return Http404("Page Not Found")


def all_squirrels(request):
    if request:
        context = {'squirrels': Sighting.objects.all()}
        return render(request, 'sightings/all.html', context)
    else:
        Http404("Page Not Found")