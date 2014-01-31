from django.contrib import admin
from sightings.models import Sighting, Jellyfish


class SightingAdmin(admin.ModelAdmin):
    list_fields = ('date', 'reporter', 'description',
                   'jellyfish', 'jellyfish_size', 'jellyfish_quantity',
                   'address', 'lat', 'lng', 'image_name', 'image')
    list_display = ('date', 'reporter', 'jellyfish', 'jellyfish_size', 'jellyfish_quantity')


admin.site.register(Sighting, SightingAdmin)
admin.site.register(Jellyfish)
