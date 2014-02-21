from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.files.base import ContentFile
from sorl.thumbnail import ImageField
from sorl.thumbnail import get_thumbnail


class Jellyfish(models.Model):
    name = models.CharField(max_length=2000)
    image = models.ImageField(upload_to="jellyfishes", max_length=1000)

    class Meta:
        verbose_name_plural = "jellyfishes"

    def __unicode__(self):
        return self.name


class Sighting(models.Model):
    reporter = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    date = models.DateField()
    description = models.TextField(null=True, blank=True)
    SPECIMEN_TYPES = (
        (0, 'Known'),
        (1, 'Other')
    )
    specimen_type = models.IntegerField(choices=SPECIMEN_TYPES, default=0)
    other_specimen_description = models.TextField(null=True, blank=True,
                                         verbose_name="Other jellyfish specimen description")
    image_name = models.CharField(max_length=3000, null=True, blank=True, verbose_name="Image name")
    image = ImageField(upload_to="user_images", max_length=3000, null=True, blank=True,
                       verbose_name="Image file")
    address = models.CharField(max_length=5000)
    lat = models.DecimalField(max_digits=22, decimal_places=20, verbose_name=_("Latitude"))
    lng = models.DecimalField(max_digits=23, decimal_places=20, verbose_name=_("Longitude"))
    jellyfish = models.ForeignKey(Jellyfish, null=True, blank=True)
    SIZES = (
        (1, '0 - 5 cm'),
        (5, '5 - 10 cm'),
        (10, '10 - 15 cm'),
        (15, '15 - 25 cm'),
        (25, '>25 cm'),
    )
    jellyfish_size = models.IntegerField(choices=SIZES, null=True, blank=True)
    QUANTITIES = (
        (2, '2-5'),
        (6, '6-10'),
        (11, '11-99'),
        (100, '>100')
    )
    jellyfish_quantity = models.IntegerField(choices=QUANTITIES, null=True, blank=True)

    class Meta:
        ordering = ['-date']

    def save(self, *args, **kwargs):
        if not self.id:
            super(Sighting, self).save(*args, **kwargs)
            image = get_thumbnail(self.image, "50x50", crop='center', quality=99)
            self.image.save(image.name, ContentFile(image.read()), True)
        super(Sighting, self).save(*args, **kwargs)
