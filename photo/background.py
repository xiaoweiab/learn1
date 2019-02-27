import requests
# from lxml import etree
from bs4 import BeautifulSoup
import time
import os

url = "http://www.jj20.com/plus/cc.php?mid=2&typeid=1&includesons=1&cc=1920x1080&totalresult=245&pageno="
for i in range(2,6):
    url = url+str(i)+"&1"
    response = requests.get(url)
    # print(response.text)
    soup =BeautifulSoup(response.text,"lxml")
    all_li = soup.find_all('li')
    for li in all_li:
        url = "http://www.jj20.com"+li.select('a')[0]['href']
        string = li.get_text().rstrip().lstrip().replace('张)1920x1080','')
        string1 = string.split('(')
        colletion_name = string1[0]
        colletion_num = string1[1]
        # print(colletion_name+"  "+colletion_num+"  "+url)
        isExists = os.path.exists(os.path.join("E:\\壁纸\\", colletion_name))
        if not isExists:
            print("建了一个名字叫做  " + colletion_name + "  的文件夹！")
            os.makedirs(os.path.join("E:\\壁纸\\", colletion_name))
        else:
            print("名字叫做  " + colletion_name + "  的文件夹已经存在了！")
        for j in range(1,int(colletion_num)):
            if i > 1:
                url = url.replace('.html',str(j)+'.html')
            response2 = requests.get(url)
            photo_url = BeautifulSoup(response2.text,"lxml").find('li',class_="show1")
            print(photo_url)
    # time.sleep(2)