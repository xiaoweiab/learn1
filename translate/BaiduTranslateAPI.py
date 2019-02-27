import requests
import hashlib
import random
import urllib


## 运行环境: window+python3.6
## 使用Python库: requests  hashlib（md5签名加密） random urllib库


def BaiDuTranslate(content):
    appid = '20170307000041649'  #百度翻译ID
    secretKey = 'JcXq9a9QwvxN2l6AhIqH'  #百度翻译秘钥
    myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    fromLang = 'zh'  #源语言 汉语
    toLang = 'en'
    salt = random.randint(32768, 65536)  #生成随机数
    sign = appid + content + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()  #使用md5生成签名变量
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        content) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
    resultPage = requests.get(myurl).json()  # 调用百度翻译API进行翻译，获得一个结果列表
    # 先对结果列表进行切片得到一个字典，再使用get方法获得翻译结果
    result_dist = resultPage.get('trans_result')[0].get('dst')
    return result_dist

if __name__ == '__main__':
    print(BaiDuTranslate("电脑"))