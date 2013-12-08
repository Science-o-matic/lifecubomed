from django.conf.urls.defaults import patterns, url
from django.conf import settings
from django.contrib.auth.views import login, logout


urlpatterns = patterns('',
                       url(r'^login/$', login, name="users.login"),
                       url(r'^logout/$', logout, name="users.logout"),

)
