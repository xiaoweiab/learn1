import requests
import hashlib
import random
import urllib
import time

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

    file_path = 'C:\\Users\\15708\\Desktop\\080424-master\\Product Catalogue\\jd'
    jd_data_file_path = 'C:\\Users\\15708\\Desktop\\080424-master\\Product Catalogue\\jd_tanslate.txt'
    jd_data = open(file_path,'r',encoding='utf-8')
    jd_data_tanslate = open(jd_data_file_path, 'a', encoding='utf-8')
    jd_data_tanslate_read = open(jd_data_file_path, 'r', encoding='utf-8')
    num = 0
    for line in jd_data:
        line_items = line.split()
        translate_item = BaiDuTranslate(line_items[2])
        translate_line = line.replace('\n','')+"    "+translate_item+"\n"
        try:
           jd_data_tanslate.write(translate_line)
        except:
           time.sleep((random.random()*3))
           print("访问错误,开始休眠")
           jd_data_tanslate.write(translate_line)

        num = num +1


    print("翻译完成")