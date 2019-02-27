import requests
from lxml import etree

file = open("E:\\知识图谱实验室\\数据集\\智联招聘职业类别.txt",'a',encoding='utf-8')
file.write("大类 ; 小类 \n")
response = requests.get("http://sou.zhaopin.com/").text
tree = etree.HTML(response)
all_div = tree.xpath('//*[@id="search_bottom_content_demo"]/div')
for div in all_div:
    catagory_name = div.xpath('.//p/a/text()')[0]
    items = div.xpath('.//h1/a/text()')
    for item in items:
        file.write(catagory_name+" ; "+item+" \n")
print("ok")
