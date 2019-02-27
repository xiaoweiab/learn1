import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from redis import Redis


redis_client = Redis(host="localhost",port=6379,db=1)


client = MongoClient('localhost', 27017)
db = client['LagouJob']
collection = db['catagory']



response = requests.get("https://www.lagou.com/").text
lll = dict()
nam_list = []
category_lists = BeautifulSoup(response, "lxml").find_all('div', class_="menu_box")
for category_list in category_lists:

        category_list_name = category_list.find('h2').get_text().lstrip().rstrip()
        menu = category_list.find('div',class_="menu_sub dn")
        # print(menu)
        job_dict = dict()
        dls = menu.find_all('dl')
        for dl in dls:
            parent = dl.find('span').get_text()
            children = dl.find_all('a')
            children_names = []
            for child in children:
                child_name = child.get_text()
                children_names.append(child_name)
                redis_client.rpush('lagou', str(child_name))
            job_dict.__setitem__(parent, children_names)
            # print(parent+"  "+str(children_names))

            lll.__setitem__(category_list_name,job_dict)
# collection.insert_one(lll)
print("ok")