import scrapy


class AgropostSpider(scrapy.Spider):
    name = 'agropost'
    allowed_domains = ['agropost.wordpress.com']
    start_urls = ['http://agropost.wordpress.com/']

    def start_requests(self):
        urls = [
            "https: // agropost.wordpress.com /"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"prices-{page}.html"
        with open(filename, "wb") as f:
            f.write(response.body)
        self.log(f"Saved file {filename}")

