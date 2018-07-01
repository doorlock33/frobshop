import os
import sqlite3
from xml.etree import ElementTree as eTree
from urllib.request import urlopen

conn = sqlite3.connect("db.sqlite3")
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS promotions(title TEXT, ean TEXT, discountprice NUMERIC, validuntil INT)')
conn.commit()
    
tree = eTree.parse(urlopen("https://supermaco.starwave.nl/api/promotions"))
cats = tree.getroot()

print ("Root of the XML is ", cats.tag)

cat_data = []

for tags in cats:
    title, ean, discountprice, validuntil = ('',) * 4
    title = tags.attrib.get('id')
    for tags_details in tags:
        if tags_details.tag == 'Title':
            title = str(tags_details.text).strip()
            print(title)
        for sub_details in tags_details: 
            if sub_details.tag == 'EAN':
                ean = str(sub_details.text).strip()
                print(ean)
            elif sub_details.tag == 'DiscountPrice':
                discountprice = str(sub_details.text).strip()
                print(discountprice)
            elif sub_details.tag == 'ValidUntil':
                validuntil = str(sub_details.text).strip()
                print(validuntil)
        
        t = (title, ean, discountprice, validuntil)
        cat_data.append(t)

        c.execute('INSERT INTO promotions(title, ean, discountprice, validuntil) VALUES (?, ?, ?, ?)', (title, ean, discountprice, validuntil))
                   
conn.commit()