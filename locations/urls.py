from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='locations'),
    path('<int:location_id>', views.location, name='location')
]
