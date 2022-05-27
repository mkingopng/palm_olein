# fix_me: sort out psql
from engine import *
import pandas as pd
import matplotlib as plt

# check the price table
with cnx.begin() as connection:
    price_data = pd.read_sql(
        '''SELECT * FROM price''',
        con=connection)

print(price_data.head())

# check the fao_data table
with cnx.begin() as connection:
    fao_data = pd.read_sql(
        '''SELECT * FROM fao_data''',
        con=connection)

print(fao_data.head())

# check the land_use_data table.
with cnx.begin() as connection:
    land_use_data = pd.read_sql(
        '''SELECT * FROM land-use-for-vegetable-crops''',
        con=connection)

print(land_use_data.head())

# todo: fix the land_use_data table name. current name throws an error
