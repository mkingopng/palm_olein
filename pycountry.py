from dataprep.clean import clean_country
import pandas as pd

pd.options.display.max_rows = 10
pd.options.display.max_columns = 100
pd.options.display.max_colwidth = 40


df = pd.read_csv('data/FAOSTAT_vegetable_oil_imports.csv')

d2 = clean_country(df, "Area", output_format="alpha-3")

print(d2.head(10))

