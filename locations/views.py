from django.shortcuts import render, get_object_or_404
from .models import Location


# Create your views here.

def index(request):
    locations = Location.objects.all()

    context = {
        'locations': locations
    }
    return render(request, 'locations/locations.html', context)


def location(request, location_id):
    location_item = get_object_or_404(Location, pk=location_id)

    context = {
        'location': location_item
    }

    return render(request, 'locations/location.html', context)
