from sights.forms import SightReportForm
from django.views.generic.edit import FormView
from sights.models import Jellyfish


class SightReportView(FormView):
    template_name = 'sight_report_form.html'
    form_class = SightReportForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(SightReportView, self).get_context_data(**kwargs)
        context['jellyfishes'] = Jellyfish.objects.all()
        return context

    def form_valid(self, form):
        sight = form.save(commit=False)
        sight.reporter_id = self.request.user.id
        sight.save()
        return super(SightReportView, self).form_valid(form)
