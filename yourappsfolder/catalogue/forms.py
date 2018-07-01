from oscar.apps.dashboard.catalogue import forms as base_forms
from django import forms
# from yourappsfolder.catalogue import forms as Product

class ProductForm(base_forms.ProductForm):

    class Meta(base_forms.ProductForm.Meta):
        # model = Product
        fields = ('EAN')
        widgets = {
            'structure': forms.HiddenInput()
        }


# 'title', 'upc', 'on_sale',
# 'short_description', 'description',
# 'out_of_stock', 'bestseller',
# 'is_new', 'is_discountable', 'structure',
# 'markdown', 'markdown_reason', 'ean',
# 'gewicht', 'price', 'brand', 
# 'afbeelding', 'shortdescription', 'fulldescription', 
# 'category', 'subcategory', 'subsubcategory'