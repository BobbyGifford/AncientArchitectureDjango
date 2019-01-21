from django.shortcuts import render, get_object_or_404
from .models import Location
from accounts.models import Profile


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
    context = {
        'add_or_update': 'Add'
    }

    if request.method == 'POST':

        new_location = Location(
            profile=Profile.objects.get(user=request.user),
            title=request.POST['title'],
            country=request.POST['country'],
            region=request.POST['region'],
            description=request.POST['description'],
            wiki_link=request.POST['wiki_link']
        )

        if 'youtube_link' in request.POST:
            parsed_link = request.POST['youtube_link']
            parsed_link.replace('watch?v=', 'embed/')
            new_location.youtube_link = parsed_link

        if 'main_image' in request.FILES:
            new_location.main_image = request.FILES['main_image']

        if 'sub_image_1' in request.FILES:
            new_location.sub_image_1 = request.FILES['sub_image_1']

        if 'sub_image_2' in request.FILES:
            new_location.sub_image_2 = request.FILES['sub_image_2']

        if 'sub_image_3' in request.FILES:
            new_location.sub_image_3 = request.FILES['sub_image_3']

        new_location.save()
        return index(request)

    return render(request, 'locations/add_location.html', context)


def edit_location(request, location_id):
    old_location = Location.objects.get(pk=location_id)
    context = {
        'add_or_update': 'Update',
        'location': old_location
    }

    if request.method == 'POST':

        old_location.title = request.POST['title']
        old_location.country = request.POST['country']
        old_location.region = request.POST['region']
        old_location.wiki_link = request.POST['wiki_link']

        if 'youtube_link' in request.POST:
            parsed_link = request.POST['youtube_link']
            parsed_link.replace('watch?v=', 'embed/')
            old_location.youtube_link = parsed_link

        if 'main_image' in request.FILES:
            old_location.main_image = request.FILES['main_image']

        if 'sub_image_1' in request.FILES:
            old_location.sub_image_1 = request.FILES['sub_image_1']

        if 'sub_image_2' in request.FILES:
            old_location.sub_image_2 = request.FILES['sub_image_2']

        if 'sub_image_3' in request.FILES:
            old_location.sub_image_3 = request.FILES['sub_image_3']

        old_location.save()

        return index(request)

    return render(request, 'locations/add_location.html', context)


def delete_location(request, location_id):
    Location.objects.filter(id=location_id).delete()
    return index(request)
