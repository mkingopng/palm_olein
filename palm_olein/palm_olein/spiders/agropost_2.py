import scrapy


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
        # fix_me: use a while loop to append a new number to the url until i get a 404 then terminate the loop
    ]

    def parse(self, response):
        # WK: the following find all h2 with the `class` attribute being 'entry-title'
        for h2 in response.xpath("//h2[@class='entry-title']"):
            title_text_raw = h2.xpath("./a[1]//text()").get()  # WKNOTE: XPATH index starts from 1
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

            next_page = response.css('li.next a::attr(href)').get()
            # todo: this is a placeholder. need to get the xpath working properly
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)


# scrapy crawl agropost_2 -O today.json
