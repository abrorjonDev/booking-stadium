from django.contrib.gis.db import models as gis_models
from django.db import models

from django.utils.translation import gettext_lazy as _

from apps.base_models import BaseModel


class Stadium(BaseModel):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    location = gis_models.PointField()  # (longitude, latitude)
    contacts = models.JSONField()
    price = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        db_table = 'stadiums'
        verbose_name = _('Stadium')
        verbose_name_plural = _('Stadiums')

    def __str__(self):
        return self.name


class Image(BaseModel):
    image = models.ImageField(upload_to='stadiums/')
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)

    def __str__(self):
        return self.stadium.name