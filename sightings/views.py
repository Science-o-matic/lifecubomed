import math
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

ITEMS_PER_PAGE = 20
class AJAXSightingListMixin(object):

     def dispatch(self, request, *args, **kwargs):
         if not request.is_ajax():
             raise http.Http404("This is an ajax view.")
         return super(AJAXSightingListMixin, self).dispatch(request, *args, **kwargs)

     def get(self, request, *args, **kwargs):
         qs = super(AJAXSightingsListView, self).get_queryset()
         qs = qs.select_related("jellyfish", "reporter")

         jellyfish_id = request.GET.get("jellyfish_id", None)
         if jellyfish_id:
             qs = qs.filter(jellyfish__id=jellyfish_id)

         total = len(qs)
         page = int(self.request.GET.get("page", 1))
         items_per_page = int(self.request.GET.get("items", ITEMS_PER_PAGE))
         pages = math.ceil(total / items_per_page)
         start = (page - 1) * items_per_page
         end = page * items_per_page
         qs = qs[start:end]
         page_total = len(qs)

         serializer = FlatSightingSerializer()
         json = serializer.serialize(qs,
                                     indent=4,
                                     fields=('pk', 'date', 'lat', 'lng', 'reporter',
                                             'jellyfish', 'jellyfish_quantity',
                                             'jellyfish_size')
                                     )
         json = '{"audios": ' + json + ",\n"
         json += '"pagination":\n{"total": %i, "pages": %i, "page": %i, "items": %i}' % (
             total, pages, page, page_total)
         return http.HttpResponse(json)


class AJAXSightingsListView(AJAXSightingListMixin, ListView):
     model = Sighting
     paginate_by = 2
