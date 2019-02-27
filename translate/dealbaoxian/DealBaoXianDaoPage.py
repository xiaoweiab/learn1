from bs4 import BeautifulSoup
import re


file_path = "C:\\Users\\15708\\Desktop\\产品页面代码1\\default118.html"
file = open(file_path,'r',encoding='utf-8')
soup = BeautifulSoup(file,"lxml")
# 抽取头部信息
product_head  = soup.find('div',class_="suspend-info")
product_name = product_head.find('h3')
print(product_name.get_text())
recommand_reason = product_head.find_all('p')
print("推荐理由：")
for p in recommand_reason:
    print(p.get_text().lstrip().rstrip())

protects = product_head.find('ul',class_="f-oh list").find_all('li')
print("产品保障：")
for protect in protects :
    print(protect.get_text())


# 抽取介绍信息
product_introduction  = soup.find('div',class_="jieshao")
list1 = product_introduction.contents
num = 1
for i in list1 :
    if num  % 4 == 0:
       print(i)
       print("==================")
    num =num +1

# print(product_introduction)
# print("基本信息 : ")
# base_info = product_introduction.find('ul').find_all('li')
# print(base_info)
# print("产品亮点 : ")
# product_highlight = product_introduction.find_all('p')
# print(product_highlight)
# print("保障内容 : ")
# product_highlight = product_introduction.find('table')
# print(product_highlight)
# print("详细条款 : ")
# product_highlight = product_introduction.find('ul',class_="tiaokuan").find_all('a')
# print(product_highlight)
# print("免责条款: ")






