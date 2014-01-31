from django import forms
from django.utils.translation import ugettext_lazy as _
from sightings.models import Sighting, Jellyfish

SPECIMEN_TYPES = Sighting.SPECIMEN_TYPES

class SightingReportForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Sighting
        fields = ['date', 'jellyfish', 'jellyfish_size', 'jellyfish_quantity',
                  'description', 'specimen_type', 'other_specimen_description',
                  'address', 'lat', 'lng',
                  'image_name', 'image'
                  ]
        widgets = {
            'address': forms.TextInput(attrs={'size': 100}),
            'lat': forms.TextInput(attrs={'size': 18, 'readonly': 'yes'}),
            'lng': forms.TextInput(attrs={'size': 18, 'readonly': 'yes'}),
            'image_name': forms.TextInput(attrs={'size': 50}),
            'specimen_type': forms.RadioSelect(choices=SPECIMEN_TYPES),
        }
