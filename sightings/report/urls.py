from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from sightings.views import SightingReportView


urlpatterns = patterns('',
                       url(r'^$', login_required(SightingReportView.as_view()),
                           name="sightings.report_sighting"),
)
