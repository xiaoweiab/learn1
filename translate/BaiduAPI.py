import re
import requests
import hashlib
import random
import urllib

def BaiDuTranslate(content):
    appid = '20170307000041649'  #百度翻译ID
    secretKey = 'JcXq9a9QwvxN2l6AhIqH'  #百度翻译秘钥
    myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    fromLang = 'zh'
    toLang = 'en'
    salt = random.randint(32768, 65536)  #生成随机数
    sign = appid + content + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()  #使用md5构造签名变量
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        content) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
    resultPage = requests.get(myurl).json()  # 调用百度翻译API进行翻译
    result_dist = resultPage.get('trans_result')[0]
    return result_dist.get('dst')

def clear_ebay_chinese_list():
    path = 'C:\\Users\\15708\\Desktop\\跨境电商数据\\eBay_Chinese_list.csv'
    ebay_chinese_list = open(path, 'r', encoding='utf-8')
    deal_list = []
    num = 1
    for line in ebay_chinese_list:
        try:
            item_list = line.split(';')
            print(str(num) + " " + item_list[2] + " | " + item_list[3] + " | " + item_list[5])
        except:
            deal_list.append(line.rstrip().lstrip())
            if len(deal_list) > 1:
                item_list1 = ''.join(deal_list).split(';')
                print(str(num) + item_list1[2] + " | " + item_list1[3] + " | " + item_list1[5])
                deal_list.clear()

        num = num + 1

def clear_ebay_chinese_all():
    path = 'C:\\Users\\15708\\Desktop\\跨境电商数据\\eBay_Chinese_all.csv'
    ebay_chinese_list = open(path, 'r', encoding='utf-8')
    deal_list = []
    num = 1
    for line in ebay_chinese_list:
        line = line.replace("\n",'')
        print(str(num)+str(line.split(';')))
        num = num +1
        if num == 100:
            break

def clear_ebay_French_all():
    path = 'C:\\Users\\15708\\Desktop\\跨境电商数据\\eBay_French_all.csv'
    ebay_chinese_list = open(path, 'r', encoding='utf-8')
    deal_list = []
    num = 1
    for line in ebay_chinese_list:
        line = line.replace("\n",'')
        item_list = line.split(';')
        item_list_string = str(num)+" | "
        item_list_string = item_list[-1]+" | "+item_list[-2]+" | "+item_list[-3]+" | "+item_list[-4]+" | "+\
                           item_list[-10]+" | "
        # item_list[-5]+" | "+item_list[-6]+" | "+item_list[-7]+" | "+item_list[-8]+" | "+ \
        # item_list[-9]+\
        num = num + 1
        if num >100:
            break
        print(item_list_string)
    print("共有"+str(num)+"条记录")

if __name__ == '__main__':
    clear_ebay_chinese_all()
    # print(BaiDuTranslate("Clearblue/Persona"))
    # clear_ebay_chinese_all()