from django.db import models
from django.contrib.auth.models import User


class Jellyfish(models.Model):
    name = models.CharField(max_length=2000)
    image = models.ImageField(upload_to="jellyfishes", max_length=1000)


class Sight(models.Model):
    reporter = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    date = models.DateField()
    description = models.TextField(null=True, blank=True)
    description_extra = models.TextField(null=True, blank=True)
    image_name = models.CharField(max_length=3000, null=True, blank=True)
    image = models.ImageField(upload_to="user_images", max_length=3000, null=True, blank=True)
    address = models.CharField(max_length=5000, null=True, blank=True)
    lat = models.DecimalField(max_digits=6, decimal_places=3)
    lng = models.DecimalField(max_digits=6, decimal_places=3)
    jellyfish = models.ForeignKey(Jellyfish)
    SIZES = (
        (1, '0 - 5 cm'),
        (5, '5 - 10 cm'),
        (10, '10 - 15 cm'),
        (15, '15 - 25 cm'),
        (25, '>25 cm'),
    )
    jellyfish_size = models.IntegerField(choices=SIZES, blank=False)
    QUANTITIES = (
        (2, '2-5'),
        (6, '6-10'),
        (11, '11-99'),
        (100, '>100')
    )
    jellyfish_quantity = models.IntegerField(choices=QUANTITIES, blank=False)
