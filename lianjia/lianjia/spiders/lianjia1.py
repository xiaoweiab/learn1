import scrapy
from scrapy.http import Request
from scrapy import Selector
from bs4 import BeautifulSoup
import requests
class GetXinfang(scrapy.Spider):
    name = 'xinfang'
    allowed_domains = ['gz.fang.lianjia.com/loupan/']
    starts_urls =[]
    def start_requests(self):
        url = "http://gz.fang.lianjia.com/loupan/pg2/"
        response = requests.get(url=url)
        max_page = BeautifulSoup(response.text,"lxml").find('div',class_="page-box house-lst-page-box")['page-data']
        start = max_page.find(':')
        end = max_page.find(',')
        num = max_page[start + 1:end]
        bash_url = "http://gz.fang.lianjia.com/loupan/"
        for i in range(1, int(num) + 1):
            url = bash_url + "pg" + str(i) + "/"
            yield Request(url, self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text,"lxml")
        all_li = soup.find('ul',id="house-lst").find_all('li')
        print("lianjia1")
        # for li in all_li:
            # title = li.find('h2').find('a').get_text().replace('\xa0','')
            # where = li.find('div',class_="where").find('span',class_="region").get_text()
            # area = li.find('div',class_="area").get_text().strip()
            # print(title)
            # print(where)
            # print(li)
