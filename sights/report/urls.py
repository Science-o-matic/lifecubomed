from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from sights.views import SightReportView


urlpatterns = patterns('',
                       url(r'^$', login_required(SightReportView.as_view())),
)
