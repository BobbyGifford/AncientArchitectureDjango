from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='locations'),
    path('<int:location_id>', views.location, name='location'),
    path('add_location', views.add_location, name='add_location'),
    path('edit_location/<int:location_id>', views.edit_location, name='edit_location')
]
