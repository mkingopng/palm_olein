"""
clean the data scraped using the scrapy Agropost spider
"""
import os
import numpy as np
import pandas as pd

pd.options.display.width = 50
pd.options.display.max_rows = 50
pd.options.display.max_columns = 3

price_json_file = '/home/noone/Documents/GitHub/palm_olein/palm_olein/290622.json'  # fix_me:
# price_json_file = os.path.join()

# fix_me: do the cleaning as part of the scraping before it ends up in df

df = pd.read_json(price_json_file)

# clean up dates
date = df['date'].dropna()  # drop Nans
date.drop([0], inplace=True)
date = date.str.split(pat=" – ", expand=True).drop(columns=1)  # split the date string into two columns, drop one
date.columns = ['date']  # rename the column
date = date[date["date"].str.match("^[0-9]+")]  # we only want dates that start with an integer
date.reset_index(drop=True, inplace=True)  # reset index

# clean up prices
prices = df['price'].astype('str').str.extractall('(\d+)').unstack().dropna().astype(int)
prices.columns = ['price']  # rename the column
prices = prices[prices.price > 100]  # remove all values < 100
prices.reset_index(drop=True, inplace=True)  # reset the index

data = [date, prices]
clean_df = pd.concat(data, axis=1)  # fix_me:

print(clean_df)
clean_df.to_csv('clean_df_290622.csv')
