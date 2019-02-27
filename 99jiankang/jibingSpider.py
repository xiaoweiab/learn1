import redis
import os
from multiprocessing import Pool
import time
import requests
import random

class jibingSpider:

    pool = redis.ConnectionPool(host='127.0.0.1',port=6379)
    client = redis.Redis(connection_pool=pool)

    def urlManage(self,keyname,href):
        self.client.hdel("jingbing",keyname)
        self.client.hset("jibing-finish",keyname,href)
        print(keyname+"成功写入jibing-finish")

    def getAllUrlUnDeal(self):
        unDealUrl = {}
        jibing = self.client.hgetall("jingbing")
        for name in jibing:
            unDealUrl.__setitem__( name.decode('utf-8'),self.client.hget("jingbing", name).decode('utf-8'))
        return unDealUrl

    def generateAllUrl(self,url):
        baseUrl  = url
        catagory = ['jianjie','zz','by','yf','lcjc','jb','zl','yshl','bfz']
        catagoryUrl = []
        for i in catagory:
            url = url + i
            catagoryUrl.append(url)
            url = baseUrl
        return catagoryUrl

    def getContent(self,url):
        time.sleep(random.random())
        response = requests.get(url)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
        else:
            print(url+"无法正常访问")


    def requestPool(self,urls):
        pool = Pool(3)
        contents = pool.map(self.getContent, urls)
        pool.close()
        pool.join()
        return contents

    def isExists(self,midrPath, folderName,name,fileType):
        path = midrPath + folderName + "\\" + name + '.'+fileType
        isExists = os.path.exists(path)
        if isExists:
            # print(name+"  ：已经存在")
            return True
        else:
            return False

    def mkdir(self,midrPath, folderName):

        isExists = os.path.exists(os.path.join(midrPath, folderName))
        if not isExists:

            os.makedirs(os.path.join(midrPath, folderName))
            print("建了一个名字叫做  " + folderName + "  的文件夹！")
            # return True
        else:
            print("名字叫做  " + folderName + "  的文件夹已经存在了！")
            # return False

    def saveToFile(self,midrPath,catagory, name,fileType, content):

        file_path = midrPath+"\\" + catagory + '\\' + name + '.'+fileType

        try:
            f = open(file_path, 'w', encoding='utf-8')
            f.write(content)
            f.close()
            # print(name + "保存完成")
        except Exception:
            print("写入错误")

if __name__ == '__main__':
    jibingspider = jibingSpider()
    unDealUrl = jibingspider.getAllUrlUnDeal()

    # for name in unDealUrl:
    #     start_time = time.time()
    #     baseUrl = unDealUrl.get(name)
    #     jibingspider.mkdir("E://99健康",name)
    #     allUrl = jibingspider.generateAllUrl(baseUrl)
    #     num = 0
    #     for url in allUrl:
    #         content = jibingspider.getContent(url)
    #         jibingspider.saveToFile("E://99健康", name, str(num), "html", content)
    #         num = num + 1
    #     # print("9个文件都成功写入文件")
    #     jibingspider.urlManage(name, baseUrl)
    #     end_time = time.time()
    #     use_time = end_time - start_time
    #     print("content采集完成,一共花取时间" + str(use_time))


    count = 0
    for name in unDealUrl:
        try:
            start_time = time.time()
            baseUrl = unDealUrl.get(name)
            jibingspider.mkdir("E://99健康", name)
            allUrl = jibingspider.generateAllUrl(baseUrl)
            contents = jibingspider.requestPool(allUrl)
            time.sleep(0.5)
            num = 0
            for content in contents:
                jibingspider.saveToFile("E://99健康", name, str(num), "html", content)
                num = num + 1

            jibingspider.urlManage(name, baseUrl)
            end_time = time.time()
            use_time = end_time - start_time
            print("content采集完成,一共花取时间" + str(use_time))
            if count % 200==0:
                print("已经爬取200个疾病,现在开始休眠")
                time.sleep(int(random.random() * 300 + 600))
            count = count + 1
        except:
            print("出现网络错误,现在开始休眠，休眠后重新开始")
            time.sleep(int(random.random() * 300 + 200))
            unDealUrl = jibingspider.getAllUrlUnDeal()
