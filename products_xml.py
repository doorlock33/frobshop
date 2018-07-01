import xmltodict
import sqlite3
from urllib.request import urlopen

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS products(ean REAL, title TEXT, brand TEXT, shortdescription TEXT, fulldescription TEXT, afbeelding TEXT, gewicht INT, price NUMERIC, category TEXT, subcategory TEXT, subsubcategory TEXT)')

def data_entry():
    with urlopen('https://supermaco.starwave.nl/api/products') as fd:
        obj = xmltodict.parse(fd.read())

    for product in obj["Products"]["Product"]:
        c.execute("INSERT INTO products VALUES (?,?,?,?,?,?,?,?,?,?,?)",(product["EAN"],product["Title"],product["Brand"],
                                                                            product["Shortdescription"],product["Fulldescription"],
                                                                            product["Image"],product["Weight"],product["Price"],
                                                                            product["Category"],product["Subcategory"],product["Subsubcategory"]))
        conn.commit()
    
create_table()
data_entry()