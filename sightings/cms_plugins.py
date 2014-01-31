from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from sightings.models import Sighting


class SightingsListPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _('Sigthings list plugin')
    render_template = "sightings_list.html"

    def render(self, context, instance, placeholder):
        context['count'] = Sighting.objects.all().count()
        context['sightings'] = Sighting.objects.all()
        return context

plugin_pool.register_plugin(SightingsListPlugin)
