# import json
# from urllib.request import urlopen

# with urlopen("https://supermaco.starwave.nl/api/products") as response:
#     source = response.read()

# data = json.loads(source)

# print(json.dumps(data))

# import pprint
# stuff = {"spam": 1, "test": 2, "testerino": 3, "abc": 4, "ni": 5}
# pprint.pprint(stuff)

# print(type(stuff))

def lucas():
    yield 2
    b = 2
    a = 1
    while True:
        yield b
        a, b = b, a + b

for x in lucas():
    print(x)