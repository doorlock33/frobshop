import os
import sqlite3
from xml.etree import ElementTree as eTree
from urllib.request import urlopen

conn = sqlite3.connect("db.sqlite3")
c = conn.cursor()


c.execute('CREATE TABLE IF NOT EXISTS categories(first_tag TEXT, second_tag TEXT, third_tag TEXT)')
conn.commit()
    
tree = eTree.parse(urlopen("https://supermaco.starwave.nl/api/categories"))
cats = tree.getroot()

print ("Root of the XML is ", cats.tag)

cat_data = []

for tags in cats:
    first_tag, second_tag, third_tag = ('',) * 3
    first_tag = tags.attrib.get('id')
    for tags_details in tags:
        if tags_details.tag == 'Name':
            first_tag = str(tags_details.text).strip()
        for sub_details in tags_details:
            if sub_details.tag == 'Name':
                second_tag = str(sub_details.text).strip()
            for subsub_details in sub_details:
                if subsub_details.tag == 'Name':
                    third_tag = str(subsub_details.text).strip()

            t = (first_tag, second_tag, third_tag)
            cat_data.append(t)

            c.execute('INSERT INTO categories(first_tag, second_tag, third_tag) VALUES (?, ?, ?)', (first_tag, second_tag, third_tag))
                   
conn.commit()

   
# for firsttag in rootElement:
#     firstname = firsttag.text
#     #print(firstname)
#     for secondtag in firsttag:
#         secondname = secondtag.text
#         #print(secondname)
#         for thirdtag in secondtag:
#             thirdname = thirdtag.text
#             #print(thirdname)
#             for fourthtag in thirdtag:
#                 fourthname = fourthtag.text
#                 #print(fourthname)

# if __name__ == "__main__":
#      data_from_element()