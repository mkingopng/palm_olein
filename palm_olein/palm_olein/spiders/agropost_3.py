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
    # it. for now, I'm more concerned with getting the damn prices right

# 558 pages
    def parse(self, response):
        entries = response.xpath('//h2')
        for entry in entries:
            yield {
                'date': entry.xpath('//div[1]/div[3]/h2[2]/a[1]//text()').extract(),
                'price': entry.xpath('//div[1]/div[3]/div[1]/table[2]/tbody/tr[2]/td[3]//text()').extract()
            }


# fix_me: need to parse better. better to get it right early in the process rather than later
# response.xpath('//div[1]/div[3]/div[1]/table[2]/tbody/tr[2]/td[3]//text()').extract()
# response.xpath('//div[1]/div[3]/div[3]/table[2]/tbody/tr[2]/td[3]//text()').extract()
# response.xpath('//div[1]/div[3]/div[5]/table[2]/tbody/tr[2]/td[3]//text()').extract()
# response.xpath('//div[1]/div[3]/div[7]/table[2]/tbody/tr[2]/td[3]//text()').extract()
# response.xpath('//div[1]/div[3]/div[9]/table[2]/tbody/tr[2]/td[3]//text()').extract()

# todo: exploring the site further, it has changed over time as WK suspected, and the structure of entries has changed.
#  What I'm working on now will work for a certain number of years but not all. Something to keep in mind.
