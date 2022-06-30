import scrapy
from scrapy import *
import pandas as pd


class AgropostSpider(scrapy.Spider):
    name = "agropost_4"

    start_urls = [
        'https://agropost.wordpress.com/',
        'https://agropost.wordpress.com/page/2/',
        'https://agropost.wordpress.com/page/3/',
        'https://agropost.wordpress.com/page/4/',
        'https://agropost.wordpress.com/page/5/',
        'https://agropost.wordpress.com/page/6/',
        'https://agropost.wordpress.com/page/7/',
        'https://agropost.wordpress.com/page/8/',
        'https://agropost.wordpress.com/page/9/',
        'https://agropost.wordpress.com/page/10/'
    ]

    def parse(self, response):
        for date in response.css('h2'):
            yield {
                'date': date.css('a::text').get(),
                'price': date.css('td::text')[3].get()
            }

# scrapy crawl agropost_4 -O today4.json

# post-14855 > table:nth-child(7) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(3)
