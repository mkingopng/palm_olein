import geojson
import geopandas
import os
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

DATA = 'data'
new_column_names = ["Year", "coconut", "cottonseed", "groundnut", "linseed", "maize", "olive", "palm", "palm kernel", "rapeseed", "safflower", "sesame", "soybean", "sunflower"]

vegetable_oil_imports = pd.read_csv(os.path.join(DATA, 'FAOSTAT_vegetable_oil_imports.csv'))
vegetable_oil_imports = vegetable_oil_imports[["Area", "Element", "Item", "Year", "Value"]]
vegetable_oil_imports.loc[vegetable_oil_imports['Element'] != 'Import Quantity'].reset_index(drop=True)
vegetable_oil_imports = vegetable_oil_imports.pivot_table(values='Value', index=['Area', 'Year'], columns="Item", aggfunc='sum').reset_index()
vegetable_oil_imports.drop('Oil, vegetable origin nes', axis=1, inplace=True)
new_column_names = ["Country", "Year", "cottonseed", "groundnut", "linseed", "maize", "olive", "palm", "palm kernel", "rapeseed", "safflower", "sesame", "soybean", "sunflower"]
vegetable_oil_imports.columns = new_column_names
vegetable_oil_imports = vegetable_oil_imports.loc[vegetable_oil_imports['Year'] == 2020]

with open("/home/noone/Documents/GitHub/palm_olein/data/countries.geojson") as f:
    world = geojson.load(f)
features = world['features'][0]
features

# fix this
veg_oil_type = 'palm'
fig = px.choropleth_mapbox(vegetable_oil_imports,
                           geojson=world,
                           locations=vegetable_oil_imports['Country'],
                           color='palm',
                           range_color=(0, 12),
                           mapbox_style="carto-positron")


fig.update_layout(title_text = f'{veg_oil_type} Vegetable Oil')

fig.show()