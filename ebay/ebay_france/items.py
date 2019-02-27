# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EbayFranceItem(scrapy.Item):
    # define the fields for your item here like:
    lists = scrapy.Field()
    print("执行item")
    pass
