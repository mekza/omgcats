# python
import datetime

# django
from django.db import models


class Gallery(models.Model):

    name = models.CharField(verbose_name="Gallery name", max_length=128)
    description = models.TextField(verbose_name="Description")

    created_at = models.DateTimeField(verbose_name="Creation date", default=datetime.datetime.now)
