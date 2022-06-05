import scrapy
import pandas as pd

# from selenium_and_firefox import date_list


class AgropostSpider(scrapy.Spider):
    name = "Agropost"
    start_urls = ["https://agropost.wordpress.com/"]

    def parse(self, response):
        for title in response.css('title'):
            yield {
                'title': title.css('title::text').get(),
            }
        for date in response.css('h2'):
            yield {
                'date': date.css('a::text').get(),
            }




# response.css('a::text')[5].get()

