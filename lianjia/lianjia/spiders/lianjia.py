import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from ..items import LianjiaItem
import requests

class Mysider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['gz.lianjia.com']

    def start_requests(self):
        theme_url = 'http://gz.lianjia.com/zufang/'
        content= requests.get(theme_url)
        soup = BeautifulSoup(content.text,"lxml")
        links = soup.find('div',class_="option-list").find_all('a')
        for link in links:
            area = link.get_text()
            if area != "不限":
                href = "http://gz.lianjia.com"+link['href']
                print("开始爬取: "+area)
                yield Request(url=href,callback=self.parse)
    def parse(self, response):
        soup = BeautifulSoup(response.text,"lxml")
        try:
          max_page = soup.find('div',class_="page-box house-lst-page-box")['page-data']
          start= max_page.find(':')
          end = max_page.find(',')
          num = max_page[start+1:end]
          bash_url = str(response.url)
          print('lianjia')
          # for i in range(1,int(num)+1):
          #     url = bash_url+"pg"+str(i)+"/"
              # yield Request(url,self.get_message)
              # print(url)
        except:
            print("没有内容")

    def get_message(self,response):
        item = LianjiaItem()
        soup = BeautifulSoup(response.text,"lxml")
        all_message = soup.find_all('div',class_="info-panel")
        # print("该页有"+str(len(all_message))+"条信息")
        lists = []
        for message in all_message:
            # item_list = item.copy()
            title = message.find('h2').find('a').get_text().replace('\xa0','')
            subway = message.find('div',class_="view-label left").get_text().replace('\xa0','')
            rental_price = message.find('div',class_="price").find('span',class_="num").get_text().replace('\xa0','')
            region = message.find('span',class_="region").get_text().replace('\xa0','')
            zone = message.find('div',class_="where").find('span',class_="zone").find('span').get_text().replace('\xa0','')
            meters = message.find('div',class_="where").find('span',class_="meters").get_text().replace('\xa0','')
            direction = message.find('div',class_="where").find_all('span')[-1].get_text().replace('\xa0','')
            other = message.find('div',class_="con").get_text().replace('\xa0','')
            list = []
            list.append(title)
            list.append(subway)
            list.append(rental_price)
            list.append(region)
            list.append(zone)
            list.append(meters)
            list.append(direction)
            list.append(other)
            lists.append(list)
        item['lists'] = lists
        yield item
        # yield item











