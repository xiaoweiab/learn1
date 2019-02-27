

import json  # 导入json模块
import requests
import hashlib

import urllib
import random


def translate():

    # appid = '20170307000041649'
    # secretKey = 'JcXq9a9QwvxN2l6AhIqH'
    appid = '20170307000041649'
    secretKey = 'JcXq9a9QwvxN2l6AhIqH'
    myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    q = '百科'
    fromLang = 'zh'
    toLang = 'en'
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
    print(myurl)
    resultPage = requests.get(myurl)  # 调用百度翻译API进行批量翻译
    print(resultPage.text)









if __name__ == '__main__':
    translate()  # 通过获得命令行参数获得输入输出文件名来执行，方便
