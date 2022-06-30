import scrapy
from scrapy import *
import pandas as pd

# from selenium_and_firefox import date_list


class AgropostSpider(scrapy.Spider):
    name = "agropost_3"

    # WK: as we have seen together, the pattern of paging is straightforward. We can keep exploring until will hit a
    #   page that shown Error 404. This logic can help you build a finite list of urls to feed here to the scrapy.Spider
    start_urls = [
        "https://agropost.wordpress.com/",
        "https://agropost.wordpress.com/page/2/",
        "https://agropost.wordpress.com/page/3/",
        "https://agropost.wordpress.com/page/4/",
        "https://agropost.wordpress.com/page/5/",
        "https://agropost.wordpress.com/page/6/",
        "https://agropost.wordpress.com/page/7/",
        "https://agropost.wordpress.com/page/8/",
        "https://agropost.wordpress.com/page/9/",
        "https://agropost.wordpress.com/page/10/"
        # fix_me: use a while loop to append a new number to the url until i get a 404 then terminate the loop
    ]

    def parse(self, response):
        entries = response.xpath('//h2')
        for entry in entries:
            yield {
                'date': entry.xpath('//div[1]/div[3]/h2[2]/a[1]//text()').extract(),  # get() works because we only want the first 'a' in the entry
                'price': entry.xpath('//table[2]/tbody/tr[2]/td[3]//text()').extract()
            }

    # fix_me: need to parse better. better to get it right early in the process rather than later



# entries = response.xpath('//h2')
# entries[4].css('a::text').get()
# entries[4].xpath('//div[1]/div[3]/h2[2]/a[1]//text()').extract()
#
# response.xpath('//div[1]/div[3]/div[1]/table[2]/tbody/tr[2]/td[3]//text()').extract()
# response.xpath('//div[1]/div[3]/div[3]/table[2]/tbody/tr[2]/td[3]//text()').extract()
# response.xpath('//div[1]/div[3]/div[5]/table[2]/tbody/tr[2]/td[3]//text()').extract()
