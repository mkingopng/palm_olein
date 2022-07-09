import os
import re
import numpy as np
import pandas as pd

pd.options.display.max_rows = 100
pd.options.display.max_columns = 50
pd.options.display.max_colwidth = 80
pd.options.display.precision = 10
pd.options.display.float_format = '{:.2f}'.format

price_df = pd.read_csv('agp5.csv')

new = price_df['date'].str.split('–', n=2, expand=True)  # it seems there is a difference between '-' and '–'. i can't tell what but python can. this is probably something that i should fix in the scraper
price_df['date'] = new[0]  # replace date with the first item in the 'new' list
price_df.drop('url', axis=1, inplace=True)  # once the scraper is debugged it's not necessary to retail the url

# price_df['date'] = pd.to_datetime(price_df['date'])  # clean up dates

# sort by date

price_df.to_csv('clean.csv')

print(price_df.head())
