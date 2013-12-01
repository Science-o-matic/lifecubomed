from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.contrib import admin
from django.views.generic import RedirectView
from django.contrib.auth.views import login, logout

admin.autodiscover()

urlpatterns = i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)


urlpatterns += patterns('',
                        url(r'^favicon\.ico$',
                            RedirectView.as_view(url=settings.STATIC_URL + 'img/favicon.ico')),
                        url(r'^gallery/', include('imagestore.urls', namespace='imagestore')),
                        url(r'^tinymce/', include('tinymce.urls')),
                        url(r'^accounts/login/$', login),
                        url(r'^accounts/logout/$', logout),

)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
