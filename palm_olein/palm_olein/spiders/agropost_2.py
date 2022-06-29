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
        # obviously i could just add more and more to this list,
        # but I don't think it's the right way
        # while a while loop to append a new number to the url
    ]

    def parse(self, response):
        for date in response.css('h2'):
            yield {
                'date': date.css('a::text').get(),  # fix_me: this works but its not robust
                'price': date.xpath('//div/table[2]/tbody/tr/td')[8].get()
            }
        # for price in response.css('table'):
        #     yield {
        #         "price": price.css('td::text')[2].get()  # fix_me: this works but its not robust
        #     }

# fix_me: need to parse better than what I am doing. this is the start of maiking it good

        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)
