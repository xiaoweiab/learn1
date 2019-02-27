import requests
from bs4 import BeautifulSoup



page_dist = dict()
response = requests.get('http://old.iachina.cn/upload/product/20091207050241328.html')
response.encoding = 'gbk'
response = response.text
p_list = BeautifulSoup(response,"lxml").find_all('p')
level = 0
for p in p_list:

    try :
        if p['align'] == "center":
           title = p.get_text()
           print("title  :  "+title)
    except:
        print(p.get_text())




