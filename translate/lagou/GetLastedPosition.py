import requests
import time
import random
import datetime
from bs4 import BeautifulSoup
from pymongo import MongoClient
import redis

client = MongoClient('60.205.229.245', 27007)
db = client['Lagou']
Mongo_db = db['position']

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
    'Cookie': 'user_trace_token=20170919133428-34842e32-9cfc-11e7-919b-5254005c3644;'
              ' LGUID=20170919133428-34843393-9cfc-11e7-919b-5254005c3644;'
              ' index_location_city=%E5%85%A8%E5%9B%BD;'
              ' _gid=GA1.2.489551564.1512647723;'
              ' _ga=GA1.2.399924787.1505799456;'
              ' Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1512647723,1512699432,1512710468,1512785411;'
              ' Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1512788669;'
              ' LGRID=20171209110429-ac07e127-dc8d-11e7-9c96-5254005c3644;'
              ' TG-TRACK-CODE=search_code;'
              ' JSESSIONID=ABAAABAAAIAACBIE33A4ECAC65A4DB3CF468D3BDC87D59C;'
              ' SEARCH_ID=6899d4adad624db4bbe6cb768482fad6',
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

    for i in range(1, 10000):
        try:
            data = {
                'first': 'true',
                'pn': i,
                'kd': keyword
            }
            position_list = list()
            try:
                datas = requests.post(url, data=data, headers=list_headers).json()
            except:
                print("访问出错，开始休眠，5秒后重新开始")
                time.sleep(5)
                print("休眠结束")
                datas = requests.post(url, data=data, headers=list_headers).json()
            content = datas['content']

            positionResult = content['positionResult']
            job_list = positionResult['result']
            list_len = len(job_list)

            for job in job_list:
                positionId = job['positionId']
                if positionId not in positionId_set:
                    try:
                        new_position = get_position_data(job,positionId,keyword=keyword)
                    except:
                        time.sleep(3)
                        new_position = get_position_data(job, positionId, keyword=keyword)
                    position_list.append(new_position)
                    positionId_set.add(positionId)

                Mongo_db.insert_many(position_list)
                print(str(i)+"成功采集")
        except:
            print(keyword+" : "+str(i)+"error")


        time.sleep(random.random()+1)
        if list_len < 15:
            print("page : "+str(i))
            break

def get_position_data(dict,positionId,keyword):
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
    # print(position_description)
    position_address = soup.find('div',class_="work_addr").get_text().replace(' ','').replace('\n','').replace('查看地图','')
    # print(position_address)


    dict.__setitem__('position_description', position_description)
    dict.__setitem__('position_address', position_address)
    dict.__setitem__('keyword', keyword)
    # print(dict)
    return dict


def main():
    # all_catagory_len = redis_client.llen('lagou')
    list = redis_client.lrange('lagou',0,273)
    catagory_name_set = set()
    for a in list:
        catagory_name_set.add(a.decode('utf-8'))
    get = {'无线产品设计师','副主编','合规稽查','销售助理','网页设计师','会计','游戏界面设计师'}
    catagory_name_set = catagory_name_set - get

    print("catagory_name初始化完成，数量："+str(len(catagory_name_set)))
    #
    url = 'https://www.lagou.com/jobs/positionAjax.json?px=new&needAddtionalResult=false&isSchoolJob=0'
    for catagory_name in catagory_name_set:
        print("开始爬取： " + catagory_name )
        get_list_data(url, catagory_name)
        print(catagory_name + " 采集完成，并写入数据库")




if __name__ == '__main__':
   main()
