# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    data = scrapy.Field()
    type = scrapy.Field()
    pass

class DoubanMovieItem(scrapy.Item):
    print("q")
    catagory = scrapy.Field()
    id = scrapy.Field()
    content = scrapy.Field()
    pass
