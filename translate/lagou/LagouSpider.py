import requests
import json
import time
import random

class LagouCrawl(object):
    def __init__(self):
        self.url = "https://www.lagou.com/jobs/positionAjax.json"
        # 请求头
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
            # "Referer": "https://www.lagou.com/jobs/list_python"
            "Referer": "https://www.lagou.com/jobs/list_java"
        }
        # 查询字符串
        self.params = {
            "city": "全国",
            "needAddtionalResult": False,
            "isSchoolJob": 0
        }
        # 表单数据
        self.data = {
            "first": True,
            "pn": 1,
            "kd": '精准推荐'
        }

    def start_crawl(self):
        response = requests.post(self.url, params=self.params, data=self.data, headers=self.headers)
        try:
            datas = response.json()
            # print(datas)
            content = datas['content']
            # print(content['pageNo'])
            print(content['pageSize'])
            hrInfoMap = content['hrInfoMap']
            print(hrInfoMap)
            # for item in hrInfoMap:
            #     print(item +"   "+str(hrInfoMap.get(item)))
            positionResult = content['positionResult']
            totalCount = positionResult['totalCount']
            print(totalCount)
            job_list = positionResult['result']
            # for job in job_list:
            #     print(job)
            time.sleep(random.random()*3+1)

        except KeyError as a:
            print(str(a))
            time.sleep(random.random()+5)





if __name__ == '__main__':
    spider = LagouCrawl()
    spider.start_crawl()

