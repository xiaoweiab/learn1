import requests
import hashlib
import random
import urllib
import time

## 运行环境: window+python3.6
## 使用Python库: requests  hashlib（md5签名加密） random urllib库
# 语言代码
# 中文	zh-CHS
# 日文	ja
# 英文	EN
# 韩文	ko
# 法文	fr
# 俄文	ru
# 葡萄牙文	pt
# 西班牙文	es

def YouDaoTranslate(content):
    appKey = '2aa4cbaa25ffaed9'  #有道翻译ID
    secretKey = '5PosiEOB78f6jdIbQlBxDSWDYNRK3gfI'  #有道翻译秘钥
    myurl = 'http://openapi.youdao.com/api'
    fromLang = 'zh-CHS'  #源语言 汉语
    toLang = 'EN'  #目标语言 汉语
    salt = random.randint(32768, 65536)  #生成随机数
    sign = appKey + content + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()  #使用md5生成签名变量
    myurl = myurl + '?appKey=' + appKey + '&q=' + urllib.parse.quote(
        content) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
    resultPage = requests.get(myurl).json()  # 调用百度翻译API进行翻译，获得一个结果列表
    # 先对结果列表进行切片得到一个字典，再使用get方法获得翻译结果
    result_dist = resultPage.get('translation')[0]
    return result_dist

if __name__ == '__main__':
    start = time.time()
    result = YouDaoTranslate("模式")
    end = time.time()
    print(result)
    print(str(end-start))

