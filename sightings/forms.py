import datetime
from django import forms
from django.utils.translation import get_language, ugettext_lazy as _
from django.utils.formats import localize_input
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

JELLYFISH_CHOICES = (
    ("ALL", _("All types")),
    ("UNKNOWN", _("Unknown type")),
)
DATEFORMATS = {'en': "%m/%d/%Y",
               "es": "%d/%m/%Y",
               }

class SightingsFilterForm(forms.Form):
    jellyfish_id = forms.ChoiceField(choices=JELLYFISH_CHOICES,
                                     label=_("Jellyfish type"))
    from_date = forms.DateField(localize=False)
    to_date = forms.DateField(localize=False)

    def __init__(self, *args, **kwargs):
        super(SightingsFilterForm, self).__init__(*args, **kwargs)

        # This is a trick, since I couldn't overwrite date formats using
        # settings.FORMAT_MODULE_PATH. DateField's widget render the date
        # was ignoring the overwrite using Django 1.5
        l = get_language()
        today = datetime.date.today()
        a_month_ago = today - datetime.timedelta(30)
        self.fields["from_date"].initial = a_month_ago.strftime(DATEFORMATS[l])
        self.fields["to_date"].initial = today.strftime(DATEFORMATS[l])

        choices = list(Jellyfish.objects.all().values_list("id", "name"))
        choices.insert(0, JELLYFISH_CHOICES[0])
        choices.append(JELLYFISH_CHOICES[1])
        self.fields['jellyfish_id'].choices = choices
