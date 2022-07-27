import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Agropost4Spider(CrawlSpider):
    name = 'agropost_4'
    idx = 1
    allowed_domains = ['agropost.wordpress.com']
    start_urls = ['http://agropost.wordpress.com/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def start_requests(self):
        for idx in range(1, 560):
            yield scrapy.Request(url=f"https://agropost.wordpress.com/page/{idx}/", callback=self.parse)


    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
