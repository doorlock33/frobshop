# yourproject/catalogue/models.py

from django.db import models

from oscar.apps.catalogue.abstract_models import AbstractProduct
from django.utils.translation import ugettext_lazy as _
from oscar.models.fields import AutoSlugField, NullCharField

class Product(AbstractProduct):
    # ean = models.TextField(max_length=250, default="", editable=True, null=True)
    # gewicht = models.TextField(max_length=250, default="", editable=True, null=True)
    # price = models.TextField(max_length=250, default="", editable=True, null=True)
    # brand = models.TextField(max_length=250, default="", editable=True, null=True)
    # afbeelding = models.URLField(max_length=200, default="", editable=True, null=True)
    # shortdescription = models.TextField(max_length=250, default="", editable=True, null=True)
    # fulldescription = models.TextField(max_length=250, default="", editable=True, null=True)
    # category = models.TextField(max_length=250, default="", editable=True, null=True)
    # subcategory = models.TextField(max_length=250, default="", editable=True, null=True)
    # subsubcategory = models.TextField(max_length=250, default="", editable=True, null=True)

    ean = NullCharField(
        _("EAN"), max_length=64, blank=True, null=True, unique=True,
        help_text=_("TEST TEST TEST TEST TEST "
                    "a product which is not specific to a particular "
                    " supplier. Eg an ISBN for a book."))

from oscar.apps.catalogue.models import *


# id, structure, upc, title, slug, description, rating, date_created, date_updated, is_dicountable, product_class_id, parent_id 