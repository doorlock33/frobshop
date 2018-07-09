import os
import sqlite3
from xml.etree import ElementTree as eTree
from urllib.request import urlopen

conn = sqlite3.connect("db.sqlite3")
c = conn.cursor()

tree = eTree.parse(urlopen("https://supermaco.starwave.nl/api/products"))
cats = tree.getroot()

print ("Root of the XML is ", cats.tag)

cat_data = []

for tags in cats:
    title, fulldescription, image, price, category = ('',) * 5
    title = tags.attrib.get('id')
    for tags_details in tags:
        if tags_details.tag == 'EAN':
            ean = str(tags_details.text).strip()
            print("EAN: ", ean)
    for tags_details in tags:
        if tags_details.tag == 'Title':
            title = str(tags_details.text).strip()
            print("Title: ", title)
    for tags_details in tags:
        if tags_details.tag == 'Brand':
            brand = str(tags_details.text).strip()
            print("Brand: ", brand)
    for tags_details in tags:
        if tags_details.tag == 'Shortdescription':
            shortdescription = str(tags_details.text).strip()
            print("Shortdescription: ", shortdescription)
    for tags_details in tags:
        if tags_details.tag == 'Fulldescription':
            fulldescription = "<p>" + str(tags_details.text).strip() + "</p>"
            print("Fulldescription: ", fulldescription)
    for tags_details in tags:
        if tags_details.tag == 'Image':
            image = str(tags_details.text).strip()
            print("Image: ", image)
    for tags_details in tags:
        if tags_details.tag == 'Weight':
            weight = str(tags_details.text).strip()
            print("Weight: ", weight)
    for tags_details in tags:
        if tags_details.tag == 'Price':
            price = str(tags_details.text).strip()
            print("Price: ", price)
    for tags_details in tags:
        if tags_details.tag == 'Category':
            category = str(tags_details.text).strip()
            print("Category: ", category)
    for tags_details in tags:
        if tags_details.tag == 'Subcategory':
            subcategory = str(tags_details.text).strip()
            print("Subcategory: ", subcategory)
    for tags_details in tags:
        if tags_details.tag == 'Subsubcategory':
            subsubcategory = str(tags_details.text).strip()
            print("Subsubcategory: ", subsubcategory)


    t = (title, fulldescription, image, price, category)
    cat_data.append(t)

    c.execute('INSERT INTO catalogue_product(title, description, image, price, category) VALUES (?, ?, ?, ?, ?)', (title, fulldescription, image, price, category))

conn.commit()


# Brand EAN Shortdescription Subcategory Subsubcategory Weight

# tree = eTree.parse(urlopen("https://supermaco.starwave.nl/api/products"))
# cats = tree.getroot()

# cat_data = []

# for tags in cats:
#     brand, ean, shortdescription, subcategory, subsubcategory, weight = ('',) * 6
#     ean = tags.attrib.get('id')
#     for tags_details in tags:
#         if tags_details.tag == 'Brand':
#             brand = str(tags_details.text).strip()
#             print("Brand: ", brand)
#     for tags_details in tags:
#         if tags_details.tag == 'EAN':
#             ean = str(tags_details.text).strip()
#             print("EAN: ", ean)
#     for tags_details in tags:
#         if tags_details.tag == 'Shortdescription':
#             shortdescription = str(tags_details.text).strip()
#             print("Shortdescription: ", shortdescription)
#     for tags_details in tags:
#         if tags_details.tag == 'Subcategory':
#             subcategory = str(tags_details.text).strip()
#             print("Subcategory: ", subcategory)
#     for tags_details in tags:
#         if tags_details.tag == 'Subsubcategory':
#             subsubcategory = str(tags_details.text).strip()
#             print("Subsubcategory: ", subsubcategory)
#     for tags_details in tags:
#         if tags_details.tag == 'Weight':
#             weight = str(tags_details.text).strip()
#             print("Weight: ", weight)

#     t = (brand, ean, shortdescription, subcategory, subsubcategory, weight)
#     cat_data.append(t)

#     c.executemany('INSERT INTO catalogue_productattributevalue(value_text) VALUES (?, ?, ?, ?, ?, ?)', (brand, ean, shortdescription, subcategory, subsubcategory, weight))

# conn.commit()

# tree = eTree.parse(urlopen("https://supermaco.starwave.nl/api/products"))
# cats = tree.getroot()

# cat_data = []

# for tags in cats:
#     ean = ('',) * 1
#     ean = tags.attrib.get('id')
#     for tags_details in tags:
#         if tags_details.tag == 'EAN':
#             ean = str(tags_details.text).strip()
#             print("EAN: ", ean)

#     t = (ean)
#     cat_data.append(t)

#     c.executemany('INSERT INTO catalogue_productattributevalue(test) VALUES (?)', (ean))

# conn.commit()
# conn.close()