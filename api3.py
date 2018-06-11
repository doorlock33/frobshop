import xmltodict
import pprint
import json
from urllib.request import urlopen

with  urlopen("https://supermaco.starwave.nl/api/categories") as fd:
    doc = xmltodict.parse(fd.read(), process_namespaces=True)

pp = pprint.PrettyPrinter()
pp.pprint(json.dumps(doc, indent=4, sort_keys=True))

pp = doc.rstrip("\n").split(",")


print(type(doc))


# https://supermaco.starwave.nl/api/categories
# https://supermaco.starwave.nl/api/promotions
# https://supermaco.starwave.nl/api/deliveryslots
# https://supermaco.starwave.nl/api/products