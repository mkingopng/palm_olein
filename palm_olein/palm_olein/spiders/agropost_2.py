import scrapy


class AgropostSpider(scrapy.Spider):
    name = "agropost_2"
    idx = 1
    domain = f"https://agropost.wordpress.com/page/{idx}/"
    # WK: as we have seen together, the pattern of paging is straightforward. We can keep exploring until will hit a
    #   page that shown Error 404. This logic can help you build a finite list of urls to feed here to the scrapy.Spider

    def start_requests(self):
        for idx in range(1, 558):
            yield scrapy.Request(url=f"https://agropost.wordpress.com/page/{idx}/", callback=self.parse)

    # todo: this works after a fashion. two problems: first, it uses a range instead of stopping at 404. the second is
    #  that the structure of the data has changed over time, as wilson predicted, so there start to be issues with the
    #  scraped data as it gets to the older posts. the problem gets progressively worse

    def parse(self, response):
        # WK: the following find all h2 with the `class` attribute being 'entry-title'
        for h2 in response.xpath("//h2[@class='entry-title']"):
            title_text_raw = h2.xpath("./a[1]//text()").get()  # WK: XPATH index starts from 1
            date_text = title_text_raw.split(' – ')[0]

            # WK: exercise for you Michael, you can try to identify the date_text being invalid to skip an iteration,
            #   so that you don't need to clean this at a later stage

            midday_closing = title_text_raw.split('\xa0')[-1]

            # WK: XPATH - get the next following sibling where the tag is "div",
            #   then drill down to the 2nd table, 2nd row and 3rd cell

            palm_olein_price = h2.xpath(".//following-sibling::div[1]/table[2]/tbody/tr[2]/td[3]//text()").get()
            yield {
                'date': date_text,
                'updated_at': midday_closing,
                'price': palm_olein_price
            }

# scrapy crawl agropost_2 -O today.json
