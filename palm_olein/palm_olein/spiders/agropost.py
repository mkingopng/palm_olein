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

# todo: i can now get a return json file which contains the information I need, plus a lot of rubbish. THat said, this
#  code feels a little less brittle than the selenium code. from what I've read, selenium was meant for website testing.
#  scrapy is intended to be a more complete web scraping solution. I'm sure its overkill for this project, but I think
#  its worth learning.
#  - currently, i need to instantiate the crawler from the scrapy command line. This is OK but I'm sure can be improved
#  - I need to get the data from json into pandas df and clean the data.

