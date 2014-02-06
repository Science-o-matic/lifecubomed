from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from sightings.views import AJAXSightingsListView


urlpatterns = patterns('',
                       url(r'^$', login_required(AJAXSightingsListView.as_view()),
                           name="sightings.locations_list"),
)
