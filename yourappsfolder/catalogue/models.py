# yourproject/catalogue/models.py

from django.db import models

from oscar.apps.catalogue.abstract_models import AbstractProduct, AbstractProductAttributeValue

class Product(AbstractProduct):
    category = models.CharField(max_length=100, blank=True, null=True, default=None)
    # subcategory = models.CharField(max_length=100, blank=True, null=True, default=None)
    # subsubcategory = models.CharField(max_length=100, blank=True, null=True, default=None)
    # ean = models.CharField(unique=True, max_length=64, blank=True, null=True, default=None)
    # weight = models.CharField(max_length=100, blank=True, null=True, default=None)
    # brand = models.TextField(blank=True, null=True, default=None)
    # shortdescription = models.TextField(blank=True, null=True, default=None)
    structure = models.CharField(max_length=10, blank=True, null=True, default=None)
    title = models.CharField(max_length=255, blank=True, null=True, default=None)
    slug = models.CharField(max_length=255, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    rating = models.FloatField(blank=True, null=True, default=None)
    date_created = models.DateTimeField(blank=True, null=True, default=None)
    date_updated = models.DateTimeField(blank=True, null=True, default=None)
    is_discountable = models.NullBooleanField(null=True)
    image = models.CharField(max_length=255, blank=True, null=True, default=None)
    price = models.TextField(blank=True, null=True, default=None)

class ProductAttributeValue(AbstractProductAttributeValue):
    value_text = models.TextField(blank=True, null=True, default=None)
    value_integer = models.IntegerField(blank=True, null=True, default=None)
    value_boolean = models.NullBooleanField(null=True)
    value_float = models.FloatField(blank=True, null=True, default=None)
    value_richtext = models.TextField(blank=True, null=True, default=None)
    value_date = models.DateField(blank=True, null=True, default=None)
    value_file = models.CharField(max_length=255, blank=True, null=True, default=None)
    value_image = models.CharField(max_length=255, blank=True, null=True, default=None)
    entity_object_id = models.PositiveIntegerField(blank=True, null=True, default=None)
    value_datetime = models.DateTimeField(blank=True, null=True, default=None)
    # test = models.CharField(max_length=255, blank=True, null=True, default=None)

from oscar.apps.catalogue.models import *

# ---------------DB FIELDS FOR AbstractProduct---------------
# id = models.IntegerField(primary_key=True)  # AutoField?
# structure = models.CharField(max_length=10)
# upc = models.CharField(unique=True, max_length=64, blank=True, null=True)
# title = models.CharField(max_length=255)
# slug = models.CharField(max_length=255)
# description = models.TextField()
# rating = models.FloatField(blank=True, null=True)
# date_created = models.DateTimeField()
# date_updated = models.DateTimeField()
# is_discountable = models.BooleanField()
# product_class = models.ForeignKey('CatalogueProductclass', models.DO_NOTHING, blank=True, null=True)
# ean = models.CharField(unique=True, max_length=64, blank=True, null=True)
# parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

# ---------------DB FIELDS FOR AbstractProductAttributeValue---------------
# id = models.IntegerField(primary_key=True)  # AutoField?
# value_text = models.TextField(blank=True, null=True)
# value_integer = models.IntegerField(blank=True, null=True)
# value_boolean = models.NullBooleanField()
# value_float = models.FloatField(blank=True, null=True)
# value_richtext = models.TextField(blank=True, null=True)
# value_date = models.DateField(blank=True, null=True)
# value_file = models.CharField(max_length=255, blank=True, null=True)
# value_image = models.CharField(max_length=255, blank=True, null=True)
# entity_object_id = models.PositiveIntegerField(blank=True, null=True)
# attribute = models.ForeignKey(CatalogueProductattribute, models.DO_NOTHING)
# entity_content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
# product = models.ForeignKey(CatalogueProduct, models.DO_NOTHING)
# value_option = models.ForeignKey(CatalogueAttributeoption, models.DO_NOTHING, blank=True, null=True)
# value_datetime = models.DateTimeField(blank=True, null=True)