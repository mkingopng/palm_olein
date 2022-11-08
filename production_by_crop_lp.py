import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

DATA = 'data'

vegetable_oil_production = pd.read_csv(os.path.join(DATA, 'vegetable-oil-production.csv'))
year = vegetable_oil_production['Year'].drop_duplicates(keep='first', inplace=False)
vegetable_oil_production = vegetable_oil_production.groupby('Year').sum(numeric_only=True)

soybean = vegetable_oil_production[
    'Crops processed - Oil, soybean - 237 - Production - 5510 - tonnes']
sesame = vegetable_oil_production[
    'Crops processed - Oil, sesame - 290 - Production - 5510 - tonnes']
linseed = vegetable_oil_production[
    'Crops processed - Oil, linseed - 334 - Production - 5510 - tonnes']
palm = vegetable_oil_production[
    'Crops processed - Oil, palm - 257 - Production - 5510 - tonnes']
rapeseed = vegetable_oil_production[
    'Crops processed - Oil, rapeseed - 271 - Production - 5510 - tonnes']
groundnut = vegetable_oil_production[
    'Crops processed - Oil, groundnut - 244 - Production - 5510 - tonnes']
cottonseed = vegetable_oil_production[
    'Crops processed - Oil, cottonseed - 331 - Production - 5510 - tonnes']
coconut = vegetable_oil_production[
    'Crops processed - Oil, coconut (copra) - 252 - Production - 5510 - tonnes']
olive_oil = vegetable_oil_production[
    'Crops processed - Oil, olive, virgin - 261 - Production - 5510 - tonnes']
safflower = vegetable_oil_production[
    'Crops processed - Oil, safflower - 281 - Production - 5510 - tonnes']
sunflower = vegetable_oil_production[
    'Crops processed - Oil, sunflower - 268 - Production - 5510 - tonnes']
maize = vegetable_oil_production[
    'Crops processed - Oil, maize - 60 - Production - 5510 - tonnes']
palm_kernel = vegetable_oil_production[
    'Crops processed - Oil, palm kernel - 258 - Production - 5510 - tonnes']

# create figure
fig = go.Figure()

# Add vectors
fig.add_trace(
    go.Scatter(x=year, y=soybean, name="soybean")),  #(soybean)
fig.add_trace(
    go.Scatter(x=year, y=sesame, name="sesame")),  # sesame
fig.add_trace(
    go.Scatter(x=year, y=linseed, name="linseed")),  # linseed
fig.add_trace(
    go.Scatter(x=year, y=palm, name="palm")),  # palm
fig.add_trace(
    go.Scatter(x=year, y=rapeseed, name="rapeseed")),  # rapeseed
fig.add_trace(
    go.Scatter(x=year, y=groundnut, name="groundnut")),  # groundnut
fig.add_trace(
    go.Scatter(x=year, y=cottonseed, name="cottonseed")),  # cottonseed
fig.add_trace(
    go.Scatter(x=year, y=coconut, name="coconut")),  # coconut
fig.add_trace(
    go.Scatter(x=year, y=olive_oil, name="olive_oil")),  # olive_oil
fig.add_trace(
    go.Scatter(x=year, y=safflower, name="safflower")),  # safflower
fig.add_trace(
    go.Scatter(x=year, y=sunflower, name="sunflower")),  # sunflower
fig.add_trace(
    go.Scatter(x=year, y=maize, name="maize")),  # maize
fig.add_trace(
    go.Scatter(x=year, y=palm_kernel, name="palm_kernel")),  # palm_kernel

# Add figure title
fig.update_layout(
    title_text="<b>Production by Crop<b>",
    title_font_size=40,
    legend_font_size=20,
    width=1000,
    height=1000
)

# Set x-axis title
fig.update_xaxes(
    title_text="<b>Year<b>",
    title_font=dict(size=30, family='Verdana', color='black'),
    tickfont=dict(family='Calibri', color='white', size=25)
)

# Set y-axes titles
fig.update_yaxes(
    title_text="<b>Metric Tons</b> ",
    title_font=dict(size=30, family='Verdana', color='black'),
    tickfont=dict(family='Calibri', color='white', size=25)
)

fig.show()