from scrapy.http import Request
from bs4 import BeautifulSoup
import scrapy
import requests
# from ..items import EbayFranceItem
import csv


class GetProduct(scrapy.Spider):
    name = 'getProduct1'
    # allowed_domains = ['www.ebay.fr']
    start_url = "http://www.ebay.com/sch/sch/allcategories/all-categories"
    writer = csv.writer(open('E:\\Documents\\ebay\\ebayeng.csv', 'a', encoding='utf-8'))
    class_name = ''

    def start_requests(self):
        # content = requests.get(self.start_url)
        # self.parse_catagory(content)
        yield Request(url=self.start_url,callback=self.parse_catagory)

    def parse_catagory(self,content):
      soup = BeautifulSoup(content.text,"lxml")
      all_a = soup.find_all('a',class_="ch")
      print("一共有 "+str(len(all_a))+" 个分类")
      # num = 0
      for a in all_a:
          class_name = a.get_text()
          href = a['href']
          for i in range(1,51):
              url = href+"?_pgn="+str(i)
              # num = num + 1
              # print(className+"  "+url)
              yield Request(url=url,callback=self.parsePage,meta={'class_name':class_name,'href':href})

    def parsePage(self,response):
        soup = BeautifulSoup(response.text, "lxml")
        all_li1 = soup.find_all('li', class_="sresult lvresult clearfix li shic")
        all_li2 = soup.find_all('li', class_="sresult lvresult clearfix li")
        all_li = all_li1 + all_li2
        num = len(all_li)
        # print("该页有 " + str(len(all_li)) + " 个商品")
        # lists = []
        for li in all_li:
            title = li.find('a', class_="vip").get_text().strip()
            url = li.find('a', class_="vip")['href']
            try:
               price = li.find('span', class_="bold").get_text().strip()
            except:
               price = "RMB 0 "
            list = []
            list.append(response.meta['class_name'])
            list.append(response.meta['href'])
            list.append(self.class_name)
            list.append(title)
            list.append(url)
            list.append(price)
            self.writer.writerow(list)
            # lists.append(list)
        # self.send_item(lists=lists)

    def send_item(self,list):
        # item = EbayFranceItem()
        # item['lists'] = lists
        # return item
        file_path = "E:\\Documents\\ebay\\ebay1.csv"
        file = open(file_path,'a',encoding='utf-8')
        file.write(list)





