import scrapy
import re
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from palm_olein.palm_olein.items import PalmOleinItem


class AgropostSpider(scrapy.Spider):
    name = "agropost_3"
    idx = 1
    allowed_domains = ['https://agropost.wordpress.com']
    start_urls = 'https://agropost.wordpress.com'

    def start_requests(self):
        for idx in range(1, 560):
            yield scrapy.Request(url=f"https://agropost.wordpress.com/page/{idx}/", callback=self.parse)

    def parse(self, response):
        pattern_1 = re.compile("[0-9]")
        datetime_pattern = re.compile(r'\d{1,2}\w{0,2} \w+ \d{2,4}')
        pattern_2 = re.compile(r"^\d\d+(\.[1-9])?$")  # ("[0-9]{3,4}]")
        for h2 in response.xpath("//h2[@class='entry-title']"):
            title_text_raw = h2.xpath("./a[1]//text()").get()
            # date_text = title_text_raw.split(' – ')[0]
            extracted = datetime_pattern.search(title_text_raw)
            date_text = extracted.group() if extracted else None
            midday_closing = title_text_raw.split('\xa0')[-1]

            second_row = h2.xpath(".//following-sibling::div[1]/table[2]/tbody/tr[2]")
            product = second_row.xpath(".//td[1]//text()").get()
            buy_or_sell = second_row.xpath(".//td[2]//text()").get()
            price = second_row.xpath(".//td[3]//text()").get()

            # WK: don't do the condition because we want to keep the raw form as much as we can
            # if h2.xpath("./a[1]//text()").get() is not None and pattern_1.match(h2.xpath("./a[1]//text()").get()):
            #     title_text_raw = h2.xpath("./a[1]//text()").get()
            #     # date_text = title_text_raw.split(' – ')[0]
            #     extracted = datetime_pattern.search(title_text_raw)
            #     date_text = extracted.group() if extracted else title_text_raw
            #     midday_closing = title_text_raw.split('\xa0')[-1]
            # else:
            #     pass
            # if pattern_2.match(h2.xpath(".//following-sibling::div[1]/table[2]/tbody/tr[2]/td[3]//text()").get()):
            #     palm_olein_price = h2.xpath(".//following-sibling::div[1]/table[2]/tbody/tr[2]/td[3]//text()").get()
            # else:
            #     pass

            # WK: we include 'raw_title', 'buy_or_sell', 'url' to help us clean the data later.
            #   you can include as many fields as possible if they may be of any potential help
            yield {
                'raw_title': title_text_raw,
                'url': response.url,
                'date': date_text,
                'updated_at': midday_closing,
                'product': product,
                'buy_or_sell': buy_or_sell,
                'price': price
            }
            # item = PalmOleinItem()
            # item["date"] = date_text
            # item["midday_closing"] = midday_closing
            # item["price"] = palm_olein_price

# scrapy crawl agropost_3 -O agp5.csv
