import requests
import json


class LagouCrawl(object):
    def __init__(self):
        self.url = "https://so.dajie.com/job/ajax/search/filter?keyword=&order=0&city=&recruitType=&salary=&experience=&page=2&positionFunction=130102&_CSRFToken=&ajax=1"
        # 请求头
        self.headers = {
        ":authority": "so.dajie.com",
        ":path": "/job/ajax/search/ filter?keyword = & order = 0 & city = & recruitType = & salary = & experience = & page = 2 & positionFunction = 130102 & _CSRFToken = & ajax = 1",
        ":scheme": "https" ,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
        "Referer": "https://so.dajie.com/job/search?positionFunction=130102&positionName=%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86%2F%E4%B8%BB%E7%AE%A1&from=job"
        }
        # 查询字符串
        self.params = {
                "order" : 0 ,
                "page" : 2 ,
                "positionFunction": 130102,
                "ajax": 1
        }


    def start_crawl(self):
        response = requests.post(self.url)
        data = response.text
        print(data)



if __name__ == '__main__':
    spider = LagouCrawl()
    spider.start_crawl()
