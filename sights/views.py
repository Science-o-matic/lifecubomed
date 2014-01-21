from sights.forms import SightReportForm
from django.views.generic.edit import FormView


class SightReportView(FormView):
    template_name = 'sight_report_form.html'
    form_class = SightReportForm
    success_url = '/'
