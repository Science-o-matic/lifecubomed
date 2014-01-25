from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class AccountRegisterApphook(CMSApp):
    name = _("Account Registration")
    urls = ["accounts.register.urls"]

apphook_pool.register(AccountRegisterApphook)
