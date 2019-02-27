from scrapy.http import Request
import scrapy
import os
# import requests
class Provider(scrapy.Spider):
    name = 'provider'
    rootdir = 'E:\\provider\\'
    # company_name = ''
    error = 1
    def start_requests(self):
        filepath = self.rootdir+'company.txt'
        company = open(filepath,'r')
        for line in company:
            inf = line.split()
            company_name = inf[0]
            link = 'http://www.gdgpo.gov.cn'+inf[1]
            path ='E:\\provider\\供应商信息\\'+company_name
            yield Request(url=link, callback=self.parse, meta={'name': company_name,'link':link})



    def parse(self, response):
        name = response.meta['name']
        content = response.text
        file_path = 'E:\\provider\\供应商信息2\\'+name+'.html'
        file_path1 = 'E:\\provider\\errorname.text'
        try:
          file = open(file_path,'w',encoding='utf-8')
          file.write(content)
          file.close()
        except:
          file_path = 'E:\\provider\\供应商信息2\\' + self.error + '.html'
          file1 = open(file_path,'w',encoding='utf-8')
          file1.write(content)
          file1.close()
          self.error= self.error+1
          file = open(file_path1, 'a', encoding='utf-8')
          file.write(name+" "+response.meta['link']+'\n')
          file.close()




