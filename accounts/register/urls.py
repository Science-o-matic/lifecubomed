from django.conf.urls.defaults import patterns, url
from registration.backends.default.views import RegistrationView

urlpatterns = patterns('',
                       url(r'^$',
                           RegistrationView.as_view(),
                           name='registration_register'),
)
