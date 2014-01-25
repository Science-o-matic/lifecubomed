from django.contrib import admin
from sights.models import Sight, Jellyfish


class SightAdmin(admin.ModelAdmin):
    list_fields = ('date', 'reporter', 'description',
                   'jellyfish', 'jellyfish_size', 'jellyfish_quantity',
                   'address', 'lat', 'lng', 'image_name', 'image')
    list_display = ('date', 'reporter', 'jellyfish', 'jellyfish_size', 'jellyfish_quantity')


admin.site.register(Sight, SightAdmin)
admin.site.register(Jellyfish)
