from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse
from django.core import serializers
from django import http
from django.views.generic.list import ListView
from sightings.models import Jellyfish, Sighting
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
        return http.HttpResponseRedirect(form.data["next"])


class AJAXListMixin(object):

     def dispatch(self, request, *args, **kwargs):
         if not request.is_ajax():
             import ipdb; ipdb.set_trace()


             raise http.Http404("This is an ajax view.")
         return super(AJAXListMixin, self).dispatch(request, *args, **kwargs)

     def get_queryset(self):
         return (
            super(AJAXListMixin, self)
            .get_queryset()
          )
          #  .filter(ajaxy_param=self.request.GET.get('some_ajaxy_param'))


     def get(self, request, *args, **kwargs):
         return http.HttpResponse(
             serializers.serialize(
                 'json',
                 self.get_queryset(),
                 indent=2,
             )
         )


class AJAXSightingsListView(AJAXListMixin, ListView):
     model = Sighting
