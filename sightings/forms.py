import datetime
from django import forms
from django.utils.translation import get_language, ugettext_lazy as _
from django.utils.formats import localize_input
from sightings.models import Sighting, Jellyfish, SPECIMEN_TYPES


class SightingReportForm(forms.ModelForm):
    required_css_class = 'required'

    id = forms.IntegerField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Sighting
        fields = ['id', 'date', 'jellyfish', 'jellyfish_size', 'jellyfish_quantity',
                  'description', 'specimen_type', 'other_specimen_description',
                  'address', 'reported_by', 'lat', 'lng',
                  'image_name', 'image'
                  ]
        widgets = {
            'address': forms.TextInput(attrs={'size': 100}),
            'lat': forms.TextInput(attrs={'size': 18, 'readonly': 'yes'}),
            'lng': forms.TextInput(attrs={'size': 18, 'readonly': 'yes'}),
            'image_name': forms.TextInput(attrs={'size': 50}),
            'specimen_type': forms.RadioSelect(choices=SPECIMEN_TYPES),
        }

    def __init__(self, *args, **kwargs):
        super(SightingReportForm, self).__init__(*args, **kwargs)
        date_format = get_date_format()
        self.fields["date"].widget = forms.widgets.DateInput(format=date_format)



JELLYFISH_CHOICES = (
    ("ALL", _("All jellyfishes")),
    ("UNKNOWN", _("Unknown type")),
)
DEFAULT_DATE_FORMAT = "%d/%m/%Y"
DATEFORMATS = {'en': "%m/%d/%Y"}
SIGHTINGS_LIMIT = 10

class SightingsFilterForm(forms.Form):
    jellyfish_id = forms.ChoiceField(choices=JELLYFISH_CHOICES,
                                     label="")
    from_date = forms.DateField(
        localize=False,
        label=_("From"),
        widget=forms.TextInput(attrs={"class": "narrow"}))
    to_date = forms.DateField(
        localize=False,
        label=_("To"),
        widget=forms.TextInput(attrs={"class": "narrow"}))


    def __init__(self, *args, **kwargs):
        super(SightingsFilterForm, self).__init__(*args, **kwargs)


        last_sightings = Sighting.objects.only("date").order_by("date")
        from_date = last_sightings.values_list("date", flat=True)[:SIGHTINGS_LIMIT][0]

        date_format = get_date_format()
        self.fields["from_date"].initial = from_date.strftime(date_format)
        today = datetime.date.today()
        self.fields["to_date"].initial = today.strftime(date_format)

        choices = list(Jellyfish.objects.all().values_list("id", "name"))
        choices.insert(0, JELLYFISH_CHOICES[0])
        choices.append(JELLYFISH_CHOICES[1])
        self.fields['jellyfish_id'].choices = choices

    def clean(self):
        cleaned_data = super(SightingsFilterForm, self).clean()
        if cleaned_data["from_date"] > cleaned_data["to_date"]:
            raise forms.ValidationError(_("Date range is wrong"))
        return cleaned_data


def get_date_format():
    # This is a trick, since I couldn't overwrite date formats using
    # settings.FORMAT_MODULE_PATH. DateField's widget was ignoring the overwrite
    # (using Django 1.5)
    try:
        return DATEFORMATS[get_language()]
    except KeyError:
        return DEFAULT_DATE_FORMAT
