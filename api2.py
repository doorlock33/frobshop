import xmltodict
import pprint
import json
from urllib.request import urlopen

with urlopen("https://supermaco.starwave.nl/api/products") as fd:
    doc = xmltodict.parse(fd.read())

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(json.dumps(doc))