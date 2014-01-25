from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class SightReportApphook(CMSApp):
    name = _("Sight Report")
    urls = ["sights.report.urls"]

apphook_pool.register(SightReportApphook)
