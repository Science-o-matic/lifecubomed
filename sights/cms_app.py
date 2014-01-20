from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class SightsApphook(CMSApp):
    name = _("Sights")
    urls = ["sights.urls"]

apphook_pool.register(SightsApphook)
