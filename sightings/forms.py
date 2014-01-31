from django import forms
from django.utils.translation import ugettext_lazy as _
from sightings.models import Sighting, Jellyfish


class SightingReportForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Sighting
        fields = ['date', 'jellyfish', 'jellyfish_size', 'jellyfish_quantity',
                  'description', 'description_extra', 'address', 'lat', 'lng',
                  'image_name', 'image'
                  ]
        widgets = {
            'address': forms.TextInput(attrs={'size': 100}),
            'lat': forms.TextInput(attrs={'size': 18, 'readonly': 'yes'}),
            'lng': forms.TextInput(attrs={'size': 18, 'readonly': 'yes'}),
            'image_name': forms.TextInput(attrs={'size': 50}),
        }
