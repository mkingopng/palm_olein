import plotly.express as px
import pandas as pd
import os
import json

DATA = 'data'
veg_oil_type = 'palm'
with open("/home/noone/Documents/GitHub/palm_olein/data/world.geojson", 'r') as f:
    world = json.load(f)

vegetable_oil_imports = pd.read_csv(os.path.join(DATA, 'FAOSTAT_vegetable_oil_imports.csv'))
vegetable_oil_imports = vegetable_oil_imports[["Area", "Element", "Item", "Year", "Value"]]
vegetable_oil_imports.loc[vegetable_oil_imports['Element'] != 'Import Quantity'].reset_index(drop=True)
vegetable_oil_imports = vegetable_oil_imports.pivot_table(values='Value', index=['Area', 'Year'], columns="Item", aggfunc='sum').reset_index()
vegetable_oil_imports.drop('Oil, vegetable origin nes', axis=1, inplace=True)
new_column_names = ["Country", "Year", "cottonseed", "groundnut", "linseed", "maize", "olive", "palm", "palm kernel", "rapeseed", "safflower", "sesame", "soybean", "sunflower"]
vegetable_oil_imports.columns = new_column_names
vegetable_oil_imports = vegetable_oil_imports.loc[vegetable_oil_imports['Year'] == 2020]
print(vegetable_oil_imports.head())


# plot
geo_fig = px.choropleth(
    vegetable_oil_imports,
    locations='Country',
    color=veg_oil_type,
    color_continuous_scale=px.colors.diverging.PiYG,
    locationmode='ISO-3',
    projection='natural earth'
)
geo_fig.update_layout(
    title_text=f'{veg_oil_type} Vegetable Oil',
)

geo_fig.show()

