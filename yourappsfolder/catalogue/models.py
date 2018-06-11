from django.db import models
from oscar.apps.catalogue.abstract_models import AbstractProduct

class Product(AbstractProduct):
    video_url = models.URLField()
    video_url = models.CharField(max_length=140, default="")

from oscar.apps.catalogue.models import *