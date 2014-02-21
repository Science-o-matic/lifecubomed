import os
import math
from django.core.serializers.json import Serializer
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse
from django import http
from django.views.generic.list import ListView
from django.utils import simplejson
from django.conf import settings
from sightings.models import Jellyfish, Sighting
from sightings.forms import SightingReportForm, SightingsFilterForm


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


THUMBNAIL_PLACEHOLDER_URL = os.path.join(settings.STATIC_URL, "img/thumb_placeholder.png")
class FlatSightingSerializer(Serializer):

    def get_dump_object(self, obj):
        thumb_url = THUMBNAIL_PLACEHOLDER_URL
        if obj.thumb:
            thumb_url = obj.thumb.url
        self._current.update({
                'id': obj._get_pk_val(),
                'date': obj.date.isoformat(),
                'image_url': thumb_url,
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
         form = SightingsFilterForm(self.request.GET)
         if form.is_valid():
             qs = self._build_qs(form)
         else:
             return http.HttpResponseBadRequest(simplejson.dumps(form.non_field_errors()))

         if int(self.request.GET.get("page", 0)):
             qs, pagination = self._paginate_qs(qs)

         serializer = FlatSightingSerializer()
         json = serializer.serialize(qs,
                                     indent=4,
                                     fields=('pk', 'date', 'lat', 'lng', 'reporter',
                                             'jellyfish', 'jellyfish_quantity',
                                             'jellyfish_size')
                                     )
         json = '{"sightings": ' + json
         if int(self.request.GET.get("page", 0)):
             json += self._render_pagination(pagination)
         json += "}"
         return http.HttpResponse(json)

     def _paginate_qs(self, qs):
         total = len(qs)
         page = int(self.request.GET.get("page", 1))
         items_per_page = int(self.request.GET.get("items", ITEMS_PER_PAGE))
         pages = math.ceil(total / items_per_page)
         start = (page - 1) * items_per_page
         end = page * items_per_page
         qs = qs[start:end]
         page_total = len(qs)
         return (qs, {"total": total,
                     "page": page,
                     "pages": pages,
                     "items": page_total})

     def _render_pagination(self, pagination):
         return ', "pagination": ' + simplejson.dumps(pagination)

     def _build_qs(self, form):
         qs = super(AJAXSightingsListView, self).get_queryset()
         qs = qs.select_related("jellyfish", "reporter")
         return self._apply_filters(qs, form)

     def _apply_filters(self, qs, form):
         jellyfish = form.cleaned_data["jellyfish_id"]
         if jellyfish != "ALL" and jellyfish != "UNKNOWN":
             qs = qs.filter(jellyfish__id=jellyfish)
         elif jellyfish == "UNKNOWN":
             pass

         qs = qs.filter(date__gte=form.cleaned_data["from_date"])
         qs = qs.filter(date__lte=form.cleaned_data["to_date"])

         return qs


class AJAXSightingsListView(AJAXSightingListMixin, ListView):
     model = Sighting
     paginate_by = 2
