from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from sights.models import Jellyfish
from sights.forms import SightReportForm


class SightReportView(FormView):
    template_name = 'sight_report_form.html'
    form_class = SightReportForm

    def get_context_data(self, **kwargs):
        context = super(SightReportView, self).get_context_data(**kwargs)
        context['jellyfishes'] = Jellyfish.objects.all()
        return context

    def form_valid(self, form):
        sight = form.save(commit=False)
        sight.reporter_id = self.request.user.id
        sight.save()
        return HttpResponseRedirect(form.data["next"])
