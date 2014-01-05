from django.conf.urls.defaults import patterns, url
from django.contrib.auth.views import logout
from django.views.generic.base import TemplateView


urlpatterns = patterns('',
                       url(r'^logout/$', logout),
                       url(r'^register/complete/$',
                           TemplateView.as_view(template_name='registration/registration_complete.html'),
                           name='registration_complete'),

)
