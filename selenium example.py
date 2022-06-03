from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

driver = webdriver.Firefox()

driver.get('https://hoopshype.com/salaries/players/')

players = driver.find_elements(by=By.XPATH, value='//td[@class="name"]')

players_list = []
for p in range(len(players)):
    players_list.append(players[p].text)

salaries = driver.find_elements(by=By.XPATH, value='//td[@class="hh-salaries-sorted"]')

salaries_list = []
for s in range(len(salaries)):
    salaries_list.append(salaries[s].text)

print(players_list)

