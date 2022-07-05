# Define here the models for your scraped items

# See documentation in: https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class PalmOleinItem(Item):
    date = Field()
    updated_at = Field()
    price = Field()


class BookstoscrapeItem(Item):
    title = Field()
    price = Field()
    rating = Field()
    availability = Field()