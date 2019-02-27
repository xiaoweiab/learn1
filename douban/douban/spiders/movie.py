# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import DoubanMovieItem

class MovieSpider(CrawlSpider):
    name = 'movie'
    allowed_domains = ['www.douban.com']
    start_urls = ['https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=0']

    rules = (
        Rule(LinkExtractor(allow='https://movie.douban.com/subject/\\d{7}'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow='https://movie.douban.com/celebrity/\\d{7}'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow='https://movie.douban.com/subject/\\d{7}/awards'), callback='parse_item', follow=True),

    )

    def parse_item(self, response):
        movieitem = DoubanMovieItem()

        url = response.url

        if 'celebrity' in url:
            movieitem['catagory'] = 'celebrity'
            movieitem['id'] = url.split('/')[-1]
        elif 'awards' in url :
            movieitem['catagory'] = 'awards'
            movieitem['id'] = url.split('/')[-2]
        else:
            movieitem['catagory'] = 'subject'
            movieitem['id'] = url.split('/')[-1]
        movieitem[' content'] = response.text

        self.logger.info(movieitem['catagory'] +" "+movieitem['id']+"  成功爬取")

        return movieitem


