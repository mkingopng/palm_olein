from urllib.request import urlopen
import json
import plotly.express as px
import pandas as pd

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv", dtype={"fips": str})


fig = px.choropleth_mapbox(
    df, geojson=counties,
    locations='fips',
    color='unemp',
    color_continuous_scale="Viridis",
    range_color=(0, 12),
    mapbox_style="carto-positron",
    zoom=3,
    center={"lat": 37.0902, "lon": -95.7129},
    opacity=0.5,
    labels={'unemp': 'unemployment rate'}
    )
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()
