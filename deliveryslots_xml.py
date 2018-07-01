import os
import sqlite3
from xml.etree import ElementTree as eTree
from urllib.request import urlopen

conn = sqlite3.connect("db.sqlite3")
c = conn.cursor()


c.execute('CREATE TABLE IF NOT EXISTS deliveryslots(datum INT, starttime INT, endtime INT, price INT)')
conn.commit()
    
tree = eTree.parse(urlopen("https://supermaco.starwave.nl/api/deliveryslots"))
cats = tree.getroot()

print ("Root of the XML is ", cats.tag)

cat_data = []

for tags in cats:
    datum, starttime, endtime, price = ('',) * 4
    datum = tags.attrib.get('id')
    for tags_details in tags:
        if tags_details.tag == 'Date':
            datum = str(tags_details.text).strip()
            print("|------Date------: ",datum," :------Date------|")
        for timeslot in tags_details:
            for sub_details in timeslot: 
                if sub_details.tag == 'StartTime':
                    starttime = str(sub_details.text).strip()
                    print("StartTime: ",starttime)
                elif sub_details.tag == 'EndTime':
                    endtime = str(sub_details.text).strip()
                    print("EndTime: ",endtime)
                elif sub_details.tag == 'Price':
                    price = str(sub_details.text).strip()
                    print("Price: ",price)
        
                t = (datum, starttime, endtime, price)
                cat_data.append(t)

            c.execute('INSERT INTO deliveryslots(datum, starttime, endtime, price) VALUES (?, ?, ?, ?)', (datum, starttime, endtime, price))
                   
conn.commit()