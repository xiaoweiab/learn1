from scrapy.http import Request
import json
import scrapy
import requests

class BaseInf(scrapy.Spider):
    name = 'baseinf'
    # start_url
    def start_requests(self):
        list = []
        path = 'E:\provider\\company.txt'
        file = open(path,'r')
        for line in file:
            company_name = line.split()[0]
            # link = "http://www.tianyancha.com/v2/search/"+company_name+".json?"
            link =  "http://www.tianyancha.com/search?key="+company_name+"&checkFrom=searchBox"
            yield Request(url=link,callback=self.parse,meta={'name':company_name})


    def parse(self, response):
        # jdict = json.loads(response.body)
        print(response.text)
        # json = response.json()
        # if json.get('data') == None:
        #     file1 = open("E:\\provider\\天眼查数据\\error.txt", 'w')
        #     file1.write(response.meta['name'])
        #
        # else:
        #     for item in json.get('data'):
        #         file1 = open("E:\\provider\\天眼查数据\\总表.txt", 'w',encoding='utf-8')
        #         file1.write(item)