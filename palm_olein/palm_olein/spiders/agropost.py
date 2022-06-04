import scrapy
import pandas as pd

# from selenium_and_firefox import date_list


class AgropostSpider(scrapy.Spider):
    name = "Agropost"
    start_urls = ["https://agropost.wordpress.com/"]

    def start_requests(self):
        urls = [
            'https://agropost.wordpress.com/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse_date(self, response):
        for head in response.css('h2').getall():
            dates_list = []
            date = head.split(" – ")[0]
            date = date.split(">")[2]
            dates_list.append(date.strip())
            print(dates_list)

    def parse_price(self, response):
        for data_tables in response.css("tables").getall():
            prices_list = []
            for table in data_tables:
                table_data = []
                rows = table.css('tr')
                for row in rows:
                    cells = row.css('td')
                    row_data = []
                    for cell in cells:
                        row_data.append(cell.text)
                    table_data.append(row_data)
                df = pd.DataFrame(table_data)
                price = df.iloc[1, 2]
                prices_list.append(price)
                print(prices_list)


# if __name__ == "__main":
#
#     request = AgropostSpider.start_requests()
#     AgropostSpider.parse_date()
#     AgropostSpider.parse_price()
#     print(dates_list)
#     browser

