from django.conf.urls.defaults import patterns, url
from sightings.views import AJAXSightingsListView


urlpatterns = patterns('',
                       url(r'^$', AJAXSightingsListView.as_view(),
                           name="sightings.locations_list"),
)
