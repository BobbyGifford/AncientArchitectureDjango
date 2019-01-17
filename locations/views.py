from django.shortcuts import render, get_object_or_404
from .models import Location


# Create your views here.

def index(request):
    locations = Location.objects.all()

    first_location = locations[0]

    context = {
        'first_location': first_location,
        'locations': locations
    }
    return render(request, 'locations/locations.html', context)


def location(request, location_id):
    location_item = get_object_or_404(Location, pk=location_id)

    context = {
        'location': location_item
    }

    return render(request, 'locations/location.html', context)


def add_location(request):
    if request.method == 'POST':
        sub_image_1 = request.FILES['sub_image_1'] if 'sub_image_1' in request.FILES else None
        sub_image_2 = request.FILES['sub_image_2'] if 'sub_image_2' in request.FILES else None
        sub_image_3 = request.FILES['sub_image_3'] if 'sub_image_3' in request.FILES else None

        # new_location = Location(
        #     title=request.POST['title'],
        #     country=request.POST['country'],
        #     region=request.POST['region'],
        #     main_image=request.FILES['main_image']
        # )

    return render(request, 'locations/add_location.html')
