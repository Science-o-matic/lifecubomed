from django.conf.urls.defaults import patterns, url
from django.contrib.auth.views import logout
from django.views.generic.base import TemplateView
from registration.backends.default.views import ActivationView


urlpatterns = patterns('',
                       url(r'^logout/$', logout),
                       url(r'^register/complete/$',
                           TemplateView.as_view(template_name='registration/registration_complete.html'),
                           name='registration_complete'),
                       url(r'^activate/complete/$',
                           TemplateView.as_view(template_name='registration/activation_complete.html'),
                           name='registration_activation_complete'),
                       url(r'^activate/(?P<activation_key>\w+)/$',
                           ActivationView.as_view(),
                           name='registration_activate'),

)
