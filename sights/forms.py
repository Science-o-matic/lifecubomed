from django import forms
from sights.models import Sight, Jellyfish


class SightReportForm(forms.ModelForm):

    class Meta:
        model = Sight
        fields = ['date', 'jellyfish', 'jellyfish_size', 'jellyfish_quantity',
                  'description', 'description_extra', 'address', 'lat', 'lng',
                  ]
