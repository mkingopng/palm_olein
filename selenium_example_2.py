from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
opts = Options()

browser = Firefox(options=opts)
browser.get('https://duckduckgo.com')

search_form = browser.find_element(by=By.ID, value='search_form_input_homepage')
search_form.send_keys('real python')
search_form.submit()
browser.implicitly_wait(5)
results = browser.find_elements(by=By.CLASS_NAME, value='result_snippet')
print(results.text)

browser.close()
quit()
