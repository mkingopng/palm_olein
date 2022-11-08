import scrapy
import re

class Agropost5Spider(scrapy.Spider):
    name = 'agropost_5'
    idx = 1
    allowed_domains = ['agropost.wordpress.com']
    start_urls = ['http://agropost.wordpress.com/']

    def start_requests(self):
        for idx in range(1, 560):
            yield scrapy.Request(url=f"https://agropost.wordpress.com/page/{idx}/", callback=self.parse)

    def parse(self, response):
        datetime_pattern = re.compile(r'\d{1,2}\w{0,2} \w+ \d{2,4}')
        for h2 in response.xpath("//h2[@class='entry-title']"):
            title_text_raw = h2.xpath("./a[1]//text()").get()
            extracted = datetime_pattern.search(title_text_raw)
            date_text = extracted.group() if extracted else None
            midday_closing = title_text_raw.split('\xa0')[-1]

            second_row = h2.xpath(".//following-sibling::div[1]/table[2]/tbody/tr[2]")
            product = second_row.xpath(".//td[1]//text()").get()
            buy_or_sell = second_row.xpath(".//td[2]//text()").get()
            price = second_row.xpath(".//td[3]//text()").get()

            yield {
                'raw_title': title_text_raw,
                'url': response.url,
                'date': date_text,
                'updated_at': midday_closing,
                'product': product,
                'buy_or_sell': buy_or_sell,
                'price': price
            }

