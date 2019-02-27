import requests
import time
import random
import datetime
from bs4 import BeautifulSoup
from pymongo import MongoClient
import redis


client = MongoClient('60.205.229.245', 27007)
db = client['Lagou']
Mongo_db1 = db['position_description_test']
Mongo_db = db['position_test']

# redis_client = redis.Redis(host='60.205.229.245',port=6379,db=1,encoding='utf-8')
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

list_headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '25',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'user_trace_token=20180111182945-f5b0366c-80c5-435a-82d8-e387ec50b4b0; _ga=GA1.2.1776576536.1515666590; _gid=GA1.2.1469427227.1515666590; LGUID=20180111182946-581b269b-f6ba-11e7-a10e-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAABEEAAJA73012D01895BCA810C9C408D2BE94E79; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1515666590,1515771590,1515860189; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1515860189; _gat=1; LGSID=20180114001628-1c49e376-f87d-11e7-a2ea-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E5%2585%25A8%25E6%25A0%2588%3Foquery%3DWP%26fromSearch%3Dtrue%26labelWords%3Drelative; LGRID=20180114001628-1c49e6b9-f87d-11e7-a2ea-5254005c3644; SEARCH_ID=d6b3cc80bcfa4cd48e25283987a20033',
    'Host': 'www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_Python?px=default&city=%E4%B8%8A%E6%B5%B7',
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': random.choice(user_agents)
}

job_page_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cache-Control':'max-age=0',
    'Host':'www.lagou.com',
    'Upgrade-Insecure-Requests':'1',
    'Cookie': '_ga=GA1.2.1184998178.1515581894; user_trace_token=20180110185812-26bf5da3-f5f5-11e7-a028-5254005c3644; LGUID=20180110185812-26bf615c-f5f5-11e7-a028-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAABEEAAJAF5FFF7F96FCD3D81D2226AAACADFF02C; _gid=GA1.2.1734321262.1515769531; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1515581895,1515665675,1515769531; LGSID=20180112230530-07aa8289-f7aa-11e7-937d-525400f775ce; PRE_UTM=; PRE_HOST=www.sogou.com; PRE_SITE=https%3A%2F%2Fwww.sogou.com%2Flink%3Furl%3DDSOYnZeCC_qqU75nxClpCQDydjxbYhws; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=index_navigation; SEARCH_ID=c5131b0a3ecb4f24b757d907a1510f47; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1515769537; LGRID=20180112230536-0b4f4db7-f7aa-11e7-a2de-5254005c3644',
    'Host': 'www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86?px=new&city=%E5%85%A8%E5%9B%BD',
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': random.choice(user_agents)
}

positionId_set= set()

def get_list_data(url,keyword):

    position_list = list()
    is_end = 0
    for i in range(1, 10000):
        data = {
                'first': 'true',
                'pn': i,
                'kd': keyword
            }
        try:
            datas = requests.get(url, data=data, headers=list_headers,timeout=3).json()
        except:
            print(keyword + "今天没有更新")
            continue


        content = datas['content']
        positionResult = content['positionResult']
        job_list = positionResult['result']

        for job in job_list:
            positionId = job['positionId']
            formatCreateTime = job['formatCreateTime']
            if '前' not in formatCreateTime:
                position_list.append(job)
                positionId_set.add(positionId)
                redis_client.sadd('LaGoupositionId',positionId)
            else:
                is_end = 1
                break
        time.sleep(random.random() + 1)
        if is_end == 1:
            break

    try:
       Mongo_db.insert_many(position_list)

    except :
       print(keyword+"今天没有更新")
    print(keyword+"  关键词采集完成，职业数量： "+ str(len(position_list))+" 累计职业数量：  " +str(len(positionId_set)))

def get_position_description(positionId):
    dict1= dict()
    time.sleep(random.random() + 1)
    url = "https://www.lagou.com/jobs/"+str(positionId)+".html"
    datas = requests.get(url,headers=job_page_headers).text
    while (len(datas) <=1759):
        print("访问出错，开始休眠，3秒后重新开始")
        time.sleep(3)
        print("休眠结束")
        datas = requests.get(url).text
    soup = BeautifulSoup(datas,"lxml")
    position_description = soup.find('dd',class_="job_bt").get_text()
    position_address = soup.find('div',class_="work_addr").get_text().replace(' ','').replace('\n','').replace('查看地图','')
    dict1.__setitem__('position_description', position_description)
    dict1.__setitem__('position_address', position_address)
    # dict.__setitem__('keyword', keyword)
    return dict1


def main():

    url = 'https://www.lagou.com/jobs/positionAjax.json?px=new&needAddtionalResult=false&isSchoolJob=0'
    num = 1
    for keyword in redis_client.sscan_iter('lagou1'):
       num = num +1
       if num <= 123:
           pass
       else:
           keyword = keyword.decode('utf-8')
           print("开始爬取： " + keyword)
           get_list_data(url, keyword)
           print(keyword + " 采集完成，并写入数据库")

    position_description_list = []
    for id in positionId_set:
        dict = get_position_description(id)
        position_description_list.append(dict)
        if len(position_description_list) == 100 :
            Mongo_db1.insert_many(position_description_list)
            position_description_list.clear()
            print("成功向MongoDB插入100条数据")
        Mongo_db1.insert_many(position_description_list)
    print("今天更新的数据采集完成，并写入数据库")


if __name__ == '__main__':
   main()
