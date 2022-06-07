"""
clean the data scraped using the scrapy Agropost spider
"""

import pandas as pd

pd.options.display.max_rows = 50
pd.options.display.max_columns = 3

price_json_file = '/home/noone/PycharmProjects/palm_olein/palm_olein/prices2.json'

df = pd.read_json(price_json_file)

# clean up dates
date = df['date'].dropna()  # drop Nans
date.drop([0], inplace=True)
date = date.str.split(pat=" – ", expand=True).drop(columns=1)  # split the date string into two columns, drop one
date.reset_index(drop=True, inplace=True)  # reset index
date.columns = ['date']  # rename the column

# clean up prices
prices = df['price'].astype('str').str.extractall('(\d+)').unstack().dropna().astype(int)
prices.columns = ['price']  # rename the column
prices = prices[prices.price > 100]  # remove all values < 100
prices.reset_index(drop=True, inplace=True)  # reset the index

data = [date, prices]
clean_df = pd.concat(data, axis=1)

print(clean_df)
clean_df.to_csv('clean_df2.csv')
