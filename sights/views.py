from sights.forms import SightReportForm
from django.views.generic.edit import FormView


class SightReportView(FormView):
    template_name = 'sight_report_form.html'
    form_class = SightReportForm
    success_url = '/'

    def form_valid(self, form):
        sight = form.save(commit=False)
        sight.reporter_id = self.request.user.id
        sight.save()
        return super(SightReportView, self).form_valid(form)
