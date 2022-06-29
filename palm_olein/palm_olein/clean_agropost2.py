"""
clean the data scraped using the scrapy Agropost spider
"""
import os
import json
import numpy as np
import pandas as pd

pd.options.display.max_rows = 50
pd.options.display.max_columns = 3

price_json_file = '/home/noone/Documents/GitHub/palm_olein/palm_olein/today.json'
# price_json_file = os.path.join('palm_olein', 'today.json')

raw_data = json.load(open(price_json_file))
df = pd.read_json(price_json_file)

# clean up dates
df2 = df.dropna(subset=['date'])  # drop Nans
df2['cleaner_date'] = df2['date'].str.split(pat=" – ", expand=True).drop(columns=1)  # split the date string into two columns, drop one
mask = df2["date"].str.match("^[0-9]+")
print(df2[~mask])
df2 = df2[mask].copy()  # we only want dates that start with an integer
df2.reset_index(drop=True, inplace=True)  # reset index

# clean up prices
# prices = df['price'].astype('str').str.extractall('(\d+)').unstack().dropna().astype(int)
# prices.columns = ['price']  # rename the column
# prices = prices[prices.price > 100]  # remove all values < 100
# prices.reset_index(drop=True, inplace=True)  # reset the index
#
# data = [date.reset_index(drop=True), prices.reset_index(drop=True)]
# clean_df = pd.concat(data, axis=1)  # problematic line

print(df2)
df2.to_csv('clean_df_290622.csv')
