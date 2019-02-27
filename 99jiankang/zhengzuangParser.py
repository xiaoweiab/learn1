from lxml import etree
import time
from pymongo import MongoClient
import os

class zhengzuangParser():

      zhengzuang_name = ''
      zhengzuang_dict = dict()

      def __init__(self,name):
          self.zhengzuang_name = name
          self.zhengzuang_dict['_id'] = name
      def parse_jianjie(self):
          file_path = 'E:\\症状\\'+self.zhengzuang_name+'\\jianjie.html'
          jianjie = open(file_path,'r',encoding='utf-8').read()
          tree = etree.HTML(jianjie)
          self.zhengzuang_dict['简介'] = tree.xpath("//div[@class='tost nickn bshare prevp curere spread graco']/p[2]/text()")

      def parse_bingyin(self):
          file_path = 'E:\\症状\\' + self.zhengzuang_name + '\\zzqy.html'
          bingyin = open(file_path, 'r', encoding='utf-8').read()
          tree = etree.HTML(bingyin)
          self.zhengzuang_dict['起因'] = tree.xpath("//div[@class='tost nickn bshare prevp curere spread graco']/p[2]/text()")+tree.xpath("//p[@style='text-indent:2em']/text()")

      def parse_yufang(self):
          file_path = 'E:\\症状\\' + self.zhengzuang_name + '\\yufang.html'
          yufang = open(file_path, 'r', encoding='utf-8').read()
          tree = etree.HTML(yufang)
          self.zhengzuang_dict['预防'] = tree.xpath("//div[@class='tost nickn bshare prevp spread graco']/p/text()")

      def parse_yufang(self):
          file_path = 'E:\\症状\\' + self.zhengzuang_name + '\\yufang.html'
          yufang = open(file_path, 'r', encoding='utf-8').read()
          tree = etree.HTML(yufang)
          self.zhengzuang_dict['预防'] = tree.xpath("//div[@class='tost nickn bshare prevp spread graco']/p/text()")

      def parse_jiancha(self):
          file_path = 'E:\\症状\\' + self.zhengzuang_name + '\\jiancha.html'
          jiancha = open(file_path, 'r', encoding='utf-8').read()
          tree = etree.HTML(jiancha)
          self.zhengzuang_dict['检查'] = tree.xpath("//div[@class='tost nickn bshare prevp spread graco']/p/text()")
          self.zhengzuang_dict['可能疾病'] = tree.xpath("//ul[@class='dissy']/li[@class='with_01']/a/text()")

      def parse_shiliao(self):
          file_path = 'E:\\症状\\' + self.zhengzuang_name + '\\shiliao.html'
          jiancha = open(file_path, 'r', encoding='utf-8').read()
          tree = etree.HTML(jiancha)
          list = tree.xpath("//div[@class='tost nickn bshare prevp spread graco']/p/text()")
          shiliaoDict = dict()
          shiliaoDict['宜吃饮食'] = list[0].split(' ')
          for elem in list:
              if '忌' in elem:
                  break_num = list.index(elem)
                  shiliaoDict['宜吃食物'] = list[1:break_num-1]
                  shiliaoDict['忌吃饮食'] = elem
                  shiliaoDict['忌吃食物']=list[break_num+1:]
          self.zhengzuang_dict['食疗'] = shiliaoDict


if __name__ == '__main__':


    start_time = time.time()
    rootdir = 'E:\\症状'
    mongoClient = MongoClient('localhost', 27017)
    datadb = mongoClient.healthPedia
    zhengzuang = datadb['zhengzuang']
    error_collection = open("E:\\zhengzuang_error.txt", 'a', encoding='utf-8')

    for parent, dirnames, filenames in os.walk(rootdir):
        for dirname in dirnames:
            try:
               zhengzuangparser = zhengzuangParser(dirname)
               zhengzuangparser.parse_jianjie()
               zhengzuangparser.parse_bingyin()
               zhengzuangparser.parse_yufang()
               zhengzuangparser.parse_jiancha()
               zhengzuangparser.parse_shiliao()
               zhengzuang.insert(zhengzuangparser.zhengzuang_dict)
            except:
                error_collection.write(dirname+"\n")


    end_time = time.time()
    print("一共花了  " + str(end_time - start_time) + " 时间")