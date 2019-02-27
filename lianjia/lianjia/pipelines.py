# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from .items import LianjiaItem
import csv





class LianjiaPipeline(object):

    # def __init__(self):

        # self.writer.writerow(['title','subway','rental_price','region','zone','meters','direction','other'])

    def process_item(self, item, spider):
        writer = csv.writer(open('E:\\lianjia1.csv', 'a'))
        lists = item['lists']
        for list in lists:
           writer.writerow(list)
        # print("执行pipeline")
        return lists





