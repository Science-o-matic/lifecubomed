from django.conf.urls.defaults import patterns, url
from django.contrib.auth.views import logout

urlpatterns = patterns('',
                       url(r'^logout/$', logout),
)
