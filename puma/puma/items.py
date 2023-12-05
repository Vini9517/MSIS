# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PumaItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    rateing =scrapy.Field()
    ram = scrapy.Field()
    battry = scrapy.Field()
    dispaly = scrapy.Field()
    processer =scrapy.Field()
    camra = scrapy.Field()
    pg = scrapy.Field()
    # org_price = scrapy.Field()
    pass
