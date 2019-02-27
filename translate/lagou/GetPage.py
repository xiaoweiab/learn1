import requests
import time
import random
import datetime
from pymongo import MongoClient
import redis
from lxml import etree

client = MongoClient('60.205.229.245', 27007)
db = client['Lagou']
catogory = db['catagory']

redis_client = redis.Redis(host='localhost',port=6379,db=1,encoding='utf-8')



user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.2995.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2986.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.0 Safari/537.36'
]

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cache-Control':'max-age=0',
    'Host':'www.lagou.com',
    'Upgrade-Insecure-Requests':'1',
    'Cookie': 'JSESSIONID=ABAAABAABEEAAJA01B659864B5E86A855DCDDA1D6A8026F;'
            'user_trace_token=20180111182945-f5b0366c-80c5-435a-82d8-e387ec50b4b0;'
            '_ga=GA1.2.1776576536.1515666590;' 
            'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1515666590;'
            '_gid=GA1.2.1469427227.1515666590; '
            'LGUID=20180111182946-581b269b-f6ba-11e7-a10e-5254005c3644; '
            'TG-TRACK-CODE=search_code; '
            'index_location_city=%E5%85%A8%E5%9B%BD; '
            'SEARCH_ID=58b544d53c1e4b20a613db86a3b0f753;'
            ' _gat=1; LGSID=20180112145804-efcd16df-f765-11e7-910c-525400f775ce; '
            'PRE_UTM=; PRE_HOST=; '
            'PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E4%25BA%25A7%25E5%2593%2581%25E7%25BB%258F%25E7%2590%2586%3Fpx%3Dnew%26city%3D%25E5%2585%25A8%25E5%259B%25BD; '
            'PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2F3308371.html; '
            'LGRID=20180112145804-efcd16df-f765-11e7-910d-525400f775ce; '
            'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1515740285,',
    'Host': 'www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86?px=new&city=%E5%85%A8%E5%9B%BD',
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': random.choice(user_agents)
}

def get_data(url):

    try:
        datas = requests.get(url,headers=headers).text
        # print(datas)
    except:
        print("访问出错，开始休眠，5秒后重新开始")
        time.sleep(5)
        print("休眠结束")
        datas = requests.get(url).text
    response = etree.HTML(datas)
    job_description = response.xpath('//*[@id="job_detail"]/dd[2]/div/p/text()')
    last_address = response.xpath('//*[@id="job_detail"]/dd[@class="job-address clearfix"]/div/text()')[3].strip()
    job_address = response.xpath('//*[@id="job_detail"]/dd[@class="job-address clearfix"]/div/a/text()')[:-1]
    job_address.append(last_address)
    print(str(job_description))
    print(str(job_address))


def main():
    url = 'https://www.lagou.com/jobs/3950057.html'
    get_data(url=url)
if __name__ == "__main__":
    main()