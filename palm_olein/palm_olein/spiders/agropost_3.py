import scrapy
import re
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from ..items import PalmOleinItem


class AgropostSpider(scrapy.Spider):
    name = "agropost_3"
    idx = 1
    allowed_domains = ['https://agropost.wordpress.com']
    start_urls = 'https://agropost.wordpress.com'
    # rules = [Rule(LinkExtractor(allow='/page/'), callback='parse', follow=True)]

    def start_requests(self):
        for idx in range(1, 558):
            yield scrapy.Request(url=f"https://agropost.wordpress.com/page/{idx}/", callback=self.parse)

    def parse(self, response):
        pattern_1 = re.compile("[0-9]")
        pattern_2 = re.compile("^\d\d+(\.[1-9])?$")  # ("[0-9]{3,4}]")
        for h2 in response.xpath("//h2[@class='entry-title']"):
            if h2.xpath("./a[1]//text()").get() is not None and pattern_1.match(h2.xpath("./a[1]//text()").get()):
                title_text_raw = h2.xpath("./a[1]//text()").get()
                date_text = title_text_raw.split(' – ')[0]
                midday_closing = title_text_raw.split('\xa0')[-1]
            else:
                pass
            if pattern_2.match(h2.xpath(".//following-sibling::div[1]/table[2]/tbody/tr[2]/td[3]//text()").get()):
                palm_olein_price = h2.xpath(".//following-sibling::div[1]/table[2]/tbody/tr[2]/td[3]//text()").get()
                # h2.xpath(".//following-sibling::div[1]/table[2]/tbody/tr[2]/td[3]//text()").get() is not None and\
            else:
                pass

            yield {
                'date': date_text,
                'updated_at': midday_closing,
                'price': palm_olein_price
            }
            # item = PalmOleinItem()
            # item["date"] = date_text
            # item["midday_closing"] = midday_closing
            # item["price"] = palm_olein_price

# scrapy crawl agropost_3 -O agp5.csv
