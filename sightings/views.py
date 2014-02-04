from django.core.serializers.json import Serializer
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse
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


class FlatSightingSerializer(Serializer):

    def get_dump_object(self, obj):
        self._current.update({
                'id': obj._get_pk_val(),
                'date': obj.date.isoformat(),
                'jellyfish': {
                    'name': unicode(obj.jellyfish) or _("N/A"),
                    'id': obj.jellyfish_id
                },
                'reporter': {
                    'name': unicode(obj.reporter),
                    'id': obj.reporter.id
                },
        })
        return self._current

class AJAXListMixin(object):

     def dispatch(self, request, *args, **kwargs):
         if not request.is_ajax():
             raise http.Http404("This is an ajax view.")
         return super(AJAXListMixin, self).dispatch(request, *args, **kwargs)

     def get(self, request, *args, **kwargs):
         serializer = FlatSightingSerializer()
         json = serializer.serialize(self.get_queryset(),
                              indent=2,
                              fields=('pk', 'date', 'lat', 'lng', 'reporter',
                                      'jellyfish', 'jellyfish_quantity',
                                      'jellyfish_size')
                              )
         return http.HttpResponse(json)



class AJAXSightingsListView(AJAXListMixin, ListView):
     model = Sighting

     def get_queryset(self):
         qs = super(AJAXSightingsListView, self).get_queryset()
         qs.select_related("jellyfish", "reporter")
         return qs
