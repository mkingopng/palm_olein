import pandas as pd
import matplotlib.pyplot as plt
import plotly as px

COUNTRY = 'India'

df = pd.read_csv('population.csv')
india_df = df[df['country_name'] == 'India']
india_df = india_df[india_df.year != 2020].copy()
print(india_df)

plt.plot('year', 'population', data=india_df)
plt.show()  # why is the line sloping in the wrong direction?

# fig = px.line(india_df, x='year', y='population')
# fig.show()