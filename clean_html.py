import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.read_csv('prices.csv')
df['raw_title'] = df['raw_title'].str.replace(' ', '')
df['price'] = df['price'].str.replace(' ', '')
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['price'] = pd.to_numeric(df['price'], errors='coerce')
cleaned_df = df

print(cleaned_df.dtypes)
print(cleaned_df)

fig = px.line(cleaned_df, x='date', y='price')
fig.show()
df.to_csv('cleaned_df.csv')

# this looks clean but there is something wrong with the plot

plt.plot('date', 'price', data=cleaned_df)
plt.show()
