from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Firefox()

driver.get('https://agropost.wordpress.com/')

# create an empty list
date_list = []
price_list = []

# grab all the tables
data_tables = driver.find_elements(by=By.TAG_NAME, value='table')  # 31 tables returned

for table in data_tables:
    table_data = []
    rows = table.find_elements(by=By.TAG_NAME, value='tr')
    for row in rows:
        cells = row.find_elements(by=By.TAG_NAME, value='td')
        row_data = []
        for cell in cells:
            row_data.append(cell.text)
        table_data.append(row_data)
    df = pd.DataFrame(table_data)
    price = df.iloc[1, 2]
    price_list.append(price)

clean_price_list = [x for x in price_list if x.isdigit() == True]
correct_price_list = clean_price_list[1::2]

# grab the post title which contains the date
post_head = driver.find_elements(by=By.TAG_NAME, value='h2')

# populate the list of dates
for p in range(len(post_head)):
    txt = post_head[p].text
    txt = txt.split(" – ")[0]
    date_list.append(txt.strip())

data_tuples = list(zip(date_list[1:], correct_price_list[1:]))
temp_df = pd.DataFrame(data_tuples, columns=["Date", "Price"])
temp_df.to_csv("palm_olein_date_and_price.csv")
print(temp_df)
