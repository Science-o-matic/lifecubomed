from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


class RemoveNextMiddleware(object):
    def process_request(self, request):
        next_url = request.GET.get('next', '')
        if settings.LOGIN_URL in next_url:
            return HttpResponseRedirect(settings.LOGIN_URL)
        if reverse('registration_activation_complete') in next_url:
            return HttpResponseRedirect(request.path)
