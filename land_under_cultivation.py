import pandas as pd
import plotly.express as px
import os

DATA = 'data'

land = pd.read_csv(os.path.join(DATA, 'land-use-palm-oil.csv'))
world_land = land.loc[land['Entity'] == 'World']
oil_palm_fruit = world_land[
    "Crops - Oil palm fruit - 254 - Area harvested - 5312 - ha"
]

fig = px.line(world_land, x="Year", y=oil_palm_fruit)

# Add figure title
fig.update_layout(
    title_text="<b>Land under Cultivation (Palm Oil)<b>",
    title_font_size=40,
    legend_font_size=20,
    width=1400,
    height=1000
)

# format x-axis
fig.update_xaxes(
    title_text="</b>Year</b>",
    title_font=dict(size=30, family='Verdana', color='black'),
    tickfont=dict(family='Calibri', color='white', size=25)
)

# Format y-axes
fig.update_yaxes(
    title_text="<b>Palm Oil Fruit (mt)</b>",
    title_font=dict(size=30, family='Verdana', color='black'),
    tickfont=dict(family='Calibri', color='white', size=25)
)

fig.show()
