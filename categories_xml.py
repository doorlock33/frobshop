import os
import sqlite3
from xml.etree import ElementTree as eTree
from urllib.request import urlopen

conn = sqlite3.connect("db.sqlite3")
c = conn.cursor()

# c.execute('ALTER TABLE catalogue_category ADD title varchar(255);')
# conn.commit()
# c.execute('ALTER TABLE catalogue_category ADD subcategory varchar(255);')
# conn.commit()
# c.execute('ALTER TABLE catalogue_category ADD subsubcategory varchar(255);')
# conn.commit()

# c.execute('CREATE TABLE IF NOT EXISTS categories(title TEXT, subcategory TEXT, subsubcategory TEXT)')
# conn.commit()

tree = eTree.parse(urlopen("https://supermaco.starwave.nl/api/categories"))
cats = tree.getroot()

print ("Root of the XML is ", cats.tag)

cat_data = []

for tags in cats:
    title, subcategory, subsubcategory = ('',) * 3
    title = tags.attrib.get('id')
    for tags_details in tags:
        if tags_details.tag == 'Name':
            title = str(tags_details.text).strip()
        for sub_details in tags_details:
            if sub_details.tag == 'Name':
                subcategory = str(sub_details.text).strip()
            for subsub_details in sub_details:
                if subsub_details.tag == 'Name':
                    subsubcategory = str(subsub_details.text).strip()

            t = (title, subcategory, subsubcategory)
            cat_data.append(t)

            c.execute('INSERT INTO catalogue_product(title, subcategory, subsubcategory) VALUES (?, ?, ?)', (title, subcategory, subsubcategory))

conn.commit()

# TITLE TERUG VERANDEREN NAAR CATEGORY