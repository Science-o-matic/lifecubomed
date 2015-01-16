from django.conf.urls.defaults import patterns, url
from sightings.views import AJAXSightingsListView


urlpatterns = patterns('',
                       url(r'^.json$', AJAXSightingsListView.as_view(),
                           name="sightings.locations_list"),
                       url(r'^/export_xls$', "sightings.views.export_xls",
                           name="sightings.export_xls"),
)
