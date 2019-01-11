from django.contrib import admin
from .models import Location


class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(Location, LocationAdmin)
