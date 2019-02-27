# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.contrib.exporter import JsonLinesItemExporter
import os

class DoubanPipeline(object):
    def process_item(self, item, spider):
        return item

class MoviePipeline(object):

    def __init__(self):
        self.path = "E://douban"
        self.create_fold(self.path)

    def process_item(self,item,spider):
        fold_path = self.path+"\\"+item['catagory']
        self.create_fold(fold_path)
        self.save_file(item['content'],fold_path,item['id'],'html')

    def create_fold(self,path):
        is_exsits = os.path.exists(path)
        if is_exsits:
            print(path+"  已经存在")
        else:
            os.mkdir(path)

    def save_file(self,content,catalog_path,file_name,file_type):
        file_path = catalog_path+"\\"+file_name+"."+file_type
        file = open(file_path,'w',encoding='utf-8')
        file.write(content)
