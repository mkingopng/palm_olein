"""
DESCRIPTION

Author: Wilson Kong
Created on: 30/4/2022
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from scrapy.selector import Selector

import time
import pandas as pd         #to save CSV file
from bs4 import BeautifulSoup
#import warnings
import warnings
warnings.filterwarnings('ignore')

# chrome_path = r'/Users/SonderJYQ05N/PycharmProjects/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("window-size=1280,800")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")

driver = webdriver.Chrome(options=options)

driver.get('https://agropost.wordpress.com/')


# grab all the tables
data_tables = driver.find_elements(by=By.TAG_NAME, value='table')  # 31 tables returned

temp_table = data_tables[0]  # is the first table CPO FUTURES PRICES
rows = temp_table.find_elements(by=By.TAG_NAME, value='tr')
table_data = []
for row in rows:
	cells = row.find_elements(by=By.TAG_NAME, value='td')
	row_data = []
	for cell in cells:
		row_data.append(cell.text)
	table_data.append(row_data)

df = pd.DataFrame(table_data)

# WK: play around to find the xpaths for the key items you want to scrape
# the following find all h2 with the `class` attribute being 'entry-title'
text = driver.page_source
all_h2_headers = Selector(text=text).xpath("//h2[@class='entry-title']")

# all_h2_headers = driver.find_elements(by=By.XPATH, value="//h2[@class='entry-title']")
h2 = all_h2_headers[0]
title_text_raw = h2.xpath("./a[1]//text()").get()  # WKNOTE: XPATH index starts from 1
date_text = title_text_raw.split(' ??? ')[0]
midday_closing = title_text_raw.split('\xa0')[-1]

# WKNOTE: XPATH - get the next following sibling where the tag is "div",
#   then drill down to the 2nd table, 2nd row and 3rd cell
palm_olein_price = h2.xpath(".//following-sibling::div[1]/table[2]/tbody/tr[2]/td[3]//text()").get()


xpath_sold_btn = "//button[@role='tab' and text()='Sold']"  # get the sold button
sold_btns = driver.find_elements(by=By.XPATH, value=xpath_sold_btn)

if sold_btns:
	sold_btns[0].click()

xpath_btn_activate_search_box = "//button[contains(@class, 'SearchButton_') and contains(@aria-haspopup, 'dialog')]"
btn_activate_search = driver.find_elements(by=By.XPATH, value=xpath_btn_activate_search_box)
if btn_activate_search:
	btn_activate_search[0].click()

xpath_search_box = "//input[@type='text' and contains(@class, 'Input')]"
input_boxes = driver.find_elements(by=By.XPATH, value=xpath_search_box)
if input_boxes:
	input_boxes[0].send_keys('Peakhurst')
	input_boxes[0].send_keys(Keys.ENTER)  # confirm the 1st item in the list
	input_boxes[0].send_keys(Keys.ENTER)  # confirm input

xpath_search_btn = "//button[@aria-label='Apply filters and search']"
search_btns = driver.find_elements(by=By.XPATH, value=xpath_search_btn)
if input_boxes:
	search_btns[0].click()


if __name__ == '__main__':
	pass
