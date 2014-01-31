from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class SightingReportApphook(CMSApp):
    name = _("Sighting Report")
    urls = ["sightings.report.urls"]

apphook_pool.register(SightingReportApphook)
