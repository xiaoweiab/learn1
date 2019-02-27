import requests
from bs4 import BeautifulSoup
import os

file = open("E:\\gupiao.txt", 'a', encoding='utf-8')
num = 1
for line in file:
    if num <=1000:
        pass
    sp = line.split()
    company_name = sp[0]
    path = company_name
    code = sp[1]
    isExists = os.path.exists(os.path.join("E:\\网易财经\\", path))
    if not isExists:
      print("建了一个名字叫做  " + path + "  的文件夹！")
      os.makedirs(os.path.join("E:\\网易财经\\", path))
    else:
      print("名字叫做  " + path + "  的文件夹已经存在了！")
    link = "http://quotes.money.163.com/trade/zjlx_" + code + ".html#01b01"
    content = requests.get(link)
    if content.status_code == 200:
       scontent = BeautifulSoup(content.text, 'lxml')
       sclist = scontent.find('div', id="menuCont").find_all('a')
       for scli in sclist[7:]:
           scurl = "http://quotes.money.163.com" + scli['href']
           scname = scli.get_text()
           print (scurl +' '+ scname)
           path = "E:\\网易财经\\"+company_name+"\\"+scname+".txt"
           content_page = requests.get(scurl)
           filepage = open(path,'w',encoding="utf-8")
           filepage.write(content_page.text)
           filepage.close()
    num = num +1









