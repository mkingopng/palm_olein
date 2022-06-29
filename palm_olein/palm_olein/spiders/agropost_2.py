import scrapy
import pandas as pd

# from selenium_and_firefox import date_list


class AgropostSpider(scrapy.Spider):
    name = "agropost_2"

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
        # fix_me: use a while loop to append a new number to the url until i get a 404 then termiate the loop
    ]

    def parse(self, response):
        for date in response.css('h2'):
            yield {
                'date': date.css('a::text').get(),
                'price': date.xpath('//div/table[2]/tbody/tr/td//text()')[8].extract()
            }

    # fix_me: need to parse better. better to get it right early in the process rather than later
