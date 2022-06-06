import json
import pandas as pd

pd.options.display.max_rows = 10
pd.options.display.max_columns = 3

with open('/home/noone/PycharmProjects/palm_olein/palm_olein/prices.json', 'r') as f:
    data = json.load(f)
    for entry in data:
        print(entry)

# print(data)
price_json_file = '/home/noone/PycharmProjects/palm_olein/palm_olein/prices.json'

df = pd.read_json(price_json_file)

print(df.head(10))
