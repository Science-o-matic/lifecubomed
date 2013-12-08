from django.conf.urls.defaults import patterns, url
from django.contrib.auth.views import login


urlpatterns = patterns('',
                       url(r'^$', login),
)
