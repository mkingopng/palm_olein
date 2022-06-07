import scrapy
import pandas as pd

# from selenium_and_firefox import date_list


class AgropostSpider(scrapy.Spider):
    name = "Agropost"
    start_urls = ["https://agropost.wordpress.com/"]

    def parse(self, response):
        for date in response.css('h2'):
            yield {
                'date': date.css('a::text').get(),  # this works
            }
        for price in response.css('table'):
            yield {
                "price": price.css('td::text')[2].get()  # this works
            }

# todo: i can now get a return json file which contains the information I need, plus a lot of rubbish.
#  - I've cleaned the results from the first page. Need to extend it to scrape more now.
#  - currently, i need to instantiate the crawler from the scrapy command line. This is OK but I'm sure can be improved


