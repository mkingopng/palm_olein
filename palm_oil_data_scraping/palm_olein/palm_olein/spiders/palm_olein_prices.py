import scrapy


class PalmOleinPricesSpider(scrapy.Spider):
    name = 'palm_olein_prices'
    allowed_domains = ['agropost.wordpress.com']
    start_urls = ['http://agropost.wordpress.com/']

    def start_requests(self):
        urls = [
            'http://agropost.wordpress.com/',
            'https://agropost.wordpress.com/2022/05/23/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')


# todo: get crawler working for daily prices from wordpress
# find <RBD Palm Olein>, two lines later we get the spot price (i think).
# need to ensure that the date field to match the price

# right now the data types for the fao data are all varchar. need to change this. correct the data types before writing
# to database. change the sql for the tables to accommodate the correct data types, and set up primary keys etc

# set up a mechanism to check for duplicates before writing to db

# automate the crawler to run once a day & update the price table

#

# todo: get database working to store information scraped by crawler

#
