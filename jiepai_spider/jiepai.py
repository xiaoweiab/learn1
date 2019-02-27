import json
import os
from hashlib import md5
from bs4 import BeautifulSoup
import requests
import re
from requests.exceptions import RequestException
from urllib.parse import urlencode
from jiepai_spider.config import *
from multiprocessing import Pool


title = ""

def getPageindex(offset,keyword):
   data={

       'offset': offset,
       'format': 'json',
       'keyword':keyword,
       'autoload': 'true',
       'count': '20',
       'cur_tab': 3

   }
   url = 'https://www.toutiao.com/search_content/?'+urlencode(data)
   try:
       response = requests.get(url)
       if response.status_code == 200:
          return response.text
   except RequestException:
       print("请求索引页出错")
       return None

def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')

def get_page_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except RequestException:
        print("请求详情页出错")
        return None

def parse_page_detail(html,url):
    global title
    soup = BeautifulSoup(html,"lxml")
    title = soup.select('title')[0].get_text()
    path = "E:\\jiepai03\\"+title
    print(title)
    mkdir(path)
    # print(fold_name)
    image_pattern = re.compile('var gallery = (.*?);',re.S)
    result = re.search(image_pattern,html)
    if result:
        data = json.loads(result.group(1))
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            for image in images:
                download_image(image)
            return {
                 'title': title,
                'url': url,
                'image':images
            }

def download_image(url):
    print("正在下载图片 ： "+url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # return response.content
            #     返回二进制内容
           save(response.content,url)
    except RequestException:
        print("请求图片出错")
        return None


def save(content,img_url):
        name = img_url[-20:-1]
        print("开始保存：" + img_url)
        file_path = "E:\\jiepai03\\"+title+"\\"+name+".jpg"
        with open(file_path, 'wb') as f:
            f.write(content)
            f.close()


def mkdir(path):
    path = path.strip()
    isExists = os.path.exists(os.path.join("E:\\jiepai03\\", path))
    if not isExists:
        print("建了一个名字叫做  " + path + "  的文件夹！")
        os.makedirs(os.path.join("E:\\jiepai03\\", path))
        return True
    else:
        print("名字叫做  " + path + "  的文件夹已经存在了！")
        return False

def main():
    html = getPageindex(0,'街拍')
    urls = parse_page_index(html)
    for url in urls:
        html = get_page_detail(url)
        if html:
            result = parse_page_detail(html,url)



if __name__== '__main__':
    pool = Pool(1)
    group = [x*20 for x in range(GROUP_START,GROUP_END+1)]
    pool.map(main(),group)
    pool.close()
    pool.join()


