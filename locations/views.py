from django.shortcuts import render
from .models import Location


# Create your views here.

def index(request):
    locations = Location.objects.all()

    context = {
        'locations': locations
    }
    return render(request, 'locations/locations.html', context)
