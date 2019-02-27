import requests
from lxml import etree
from bs4 import BeautifulSoup
import redis

pool =redis.ConnectionPool(host='127.0.0.1',port=6379)
re = redis.Redis(connection_pool=pool)
response = requests.get("http://jb.9939.com/map/")
response.encoding = "utf-8"
# print(response.text)
soup = BeautifulSoup(response.text,"lxml").find_all('div',class_="life_con")
all_li = soup[3].find_all('li',class_="cc")

num = 0
for li in all_li:
    print("==================================================")
    # print(li)
    keshi = li.find('span',class_="ks_left").get_text()
    print(keshi)
#
    all_a = li.find_all('a',target="_blank")
    for a in all_a:
        print(a)
        name = a.get_text()
        href = a['href']
        print(name+"   "+href)
        re.hset('zhengzuang', name, href)
        num = num +1
print("共有"+str(num)+"个疾病,成功写入redis数据库")





