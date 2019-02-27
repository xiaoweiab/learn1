# -*- coding: utf-8 -*-
import scrapy


class ZhengzuangSpider(scrapy.Spider):
    name = 'zhengzuang'
    allowed_domains = ['www.9399.com']
    start_urls = ['http://www.9399.com/']

    def parse(self, response):
        pass
