import json

with open('/home/noone/PycharmProjects/palm_olein/palm_olein/prices.json', 'r') as f:
    data = json.load(f)
    for entry in data:
        print(entry)
