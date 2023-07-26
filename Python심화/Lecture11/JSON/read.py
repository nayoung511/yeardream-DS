import json

with open('JSON/test.json', "r") as fd:
    obj = json.load(fd)

print(obj['소지물'][0])