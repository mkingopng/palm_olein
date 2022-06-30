import scrapy
from scrapy import *
import pandas as pd


class AgropostSpider(scrapy.Spider):
    name = "agropost_3"

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

    # WK: as we have seen together, the pattern of paging is straightforward. We can keep exploring until will hit a
    #   page that shown Error 404. This logic can help you build a finite list of urls to feed here to the scrapy.Spider

    # MK: I've tried the loop idea, and it won't work. scrapy doesn't like iterables in this location. Reading the
    # documentation, it's not as simple as we thought. there are a few ways that it could be done. one is to incorporate
    # it in the parse function, another is to use the exception handling functionality in middleware. I'll think about
    # it. for now, I'm more concerned with getting the damn prices right.

# 558 pages
    def parse(self, response):
        for date in response.css('h2'):
            yield {
                'date': date.css('a::text').get(),
                # 'price': date.css('td::text')[2].get()
            }

    # def parse(self, response):
    #     entries = response.xpath('//h2')
    #     for entry in entries:
    #         date = 1
    #         price = 1
    #         date_str = str(date)
    #         price_str = str(price)
    #         yield {
    #             'date': entry.xpath(f'//div[1]/div[3]/h2[{date_str}]/a[1]//text()').extract(),
    #             'price': entry.xpath(f'//div[1]/div[3]/div[{price_str}]/table[2]/tbody/tr[2]/td[3]//text()').extract()
    #         }
    #         date += 1
    #         price += 2


# fix_me: need to parse better. better to get it right early in the process rather than later

# tables CSS
# post-14849 > table:nth-child(7) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(3)

# dates
# /div[1]/div[3]/h2[2]/a[1]
# /div[1]/div[3]/h2[3]/a[1]

# prices - these are 'hard' xpath. I can use them to select a single data point but I can't figure out how to use them
# to iterate through a web page
# response.xpath('//div[1]/div[3]/div[1]/table[2]/tbody/tr[2]/td[3]//text()').extract()
# response.xpath('//div[1]/div[3]/div[3]/table[2]/tbody/tr[2]/td[3]//text()').extract()
# response.xpath('//div[1]/div[3]/div[5]/table[2]/tbody/tr[2]/td[3]//text()').extract()
# response.xpath('//div[1]/div[3]/div[7]/table[2]/tbody/tr[2]/td[3]//text()').extract()
# response.xpath('//div[1]/div[3]/div[9]/table[2]/tbody/tr[2]/td[3]//text()').extract()

# todo: exploring the site further, it has changed over time as WK suspected, and the structure of entries has changed.
#  What I'm working on now will work for a certain number of years but not all. Something to keep in mind

# scrapy crawl agropost_3 -O output_3.json

# response.xpath('//*[@class="entry-title"]')  # this works and could be a replacement for the date css

# response.xpath('//*[@class="entry-content"]')

# response.xpath('//*[@id="post-14851"]')  # this works for a single post, but need to do some kind of regex so it doesn't have a specific id number
