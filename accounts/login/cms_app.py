from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class AccountLoginApphook(CMSApp):
    name = _("AccountLogin")
    urls = ["accounts.login.urls"]

apphook_pool.register(AccountLoginApphook)
