"""
clean the data scraped using the scrapy agropost spider

this needs to be moved into pipelines once its performing correctly
"""
import os
import json
import numpy as np
import pandas as pd

pd.options.display.max_rows = 100
pd.options.display.max_columns = 50
pd.options.display.max_colwidth = 80
pd.options.display.precision = 10
pd.options.display.float_format = '{:.2f}'.format

price_json_file = '/home/noone/Documents/GitHub/palm_olein/palm_olein/output_1.json'
# price_json_file = os.path.join('palm_olein', 'palm_olein', 'output_1.json')

raw_data = json.load(open(price_json_file))
df = pd.read_json(price_json_file)

# clean up dates
df2 = df.dropna(subset=['date'])  # drop Nans
df2['cleaner_date'] = df2['date'].str.split(pat=" – ", expand=True).drop(columns=1)  # split the date string into two columns, drop one
mask = df2["date"].str.match("^[0-9]+")
print(df2[~mask])
df2 = df2[mask].copy()  # we only want dates that start with an integer
df2.reset_index(drop=True, inplace=True)  # reset index

print(df2)
df2.to_csv('clean_df_290622.csv')
