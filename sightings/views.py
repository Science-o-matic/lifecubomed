from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from sightings.models import Jellyfish
from sightings.forms import SightingReportForm


class SightingReportView(FormView):
    template_name = 'sighting_report_form.html'
    form_class = SightingReportForm

    def get_context_data(self, **kwargs):
        context = super(SightingReportView, self).get_context_data(**kwargs)
        context['jellyfishes'] = Jellyfish.objects.all()
        return context

    def form_valid(self, form):
        sighting = form.save(commit=False)
        sighting.reporter_id = self.request.user.id
        sighting.save()
        return HttpResponseRedirect(form.data["next"])
