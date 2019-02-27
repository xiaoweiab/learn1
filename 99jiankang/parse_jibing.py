from lxml import etree
import os
from pymongo import MongoClient
import time
class jibing_parse():

    jibing_dict = dict()
    jibing_name = ''

    def __init__(self,name):
        self.jibing_name = name
        self.jibing_dict['_id'] = name
        # self.mongoClient=MongoClient('localhost',27017)
        # self.datadb = self.mongoClient.healthPedia
        # self.illness = self.datadb['illness']


    def jianjie_parse(self):
        file_path = "E:\\疾病\\"+self.jibing_name+"\\0.html"
        jianjie = open(file_path,'r',encoding='utf-8').read()
        tree = etree.HTML(jianjie)
        self.jibing_dict['简介'] = tree.xpath("//div[@class='tost bshare spread graco']/p/text()")[0]
        self.jibing_dict['是否属于医保'] = tree.xpath("//div[@class='protex clearfix']/p[1]/text()")
        self.jibing_dict['别名'] = tree.xpath("//div[@class='protex clearfix']/p[2]/a/@title")
        self.jibing_dict['发病部位'] = tree.xpath("//div[@class='protex clearfix']/p[3]/a/text()")
        self.jibing_dict['传染性'] = tree.xpath("//div[@class='protex clearfix']/p[4]/text()")
        self.jibing_dict['传播途径'] = tree.xpath("//div[@class='protex clearfix']/p[5]/text()")
        self.jibing_dict['多发人群'] = tree.xpath("//div[@class='protex clearfix']/p[6]/text()")
        self.jibing_dict['典型症状'] = tree.xpath("//div[@class='protex clearfix']/div[1]/div[@class='stat disn']/a/@title")
        self.jibing_dict['相关疾病'] = tree.xpath("//div[@class='protex clearfix']/div[2]/div[@class='stat disn']/a/@title")
        self.jibing_dict['就诊科室'] = tree.xpath("//div[@class='tost nickn aknol graco']/p[1]/a/text()")
        self.jibing_dict['治疗方法'] = tree.xpath("//div[@class='tost nickn aknol graco']/p[2]/text()")[0].split(' ')
        self.jibing_dict['常用药品'] = tree.xpath("//div[@class='refl']/div/a/text()")

    def zhengzhuang_parse(self):
        file_path = "E:\\疾病\\" + self.jibing_name + "\\1.html"
        zhengzhuang = open(file_path, 'r', encoding='utf-8').read()
        tree = etree.HTML(zhengzhuang)
        self.jibing_dict['典型症状1'] = tree.xpath("//div[@class='tost nickn bshare spread graco']/p[1]/a/text()")
        self.jibing_dict['症状内容'] = tree.xpath("//p[@class='spea']/text()")+tree.xpath("//p[@style='text-indent:2em']/text()")

    def bingyin_parse(self):
        file_path = "E:\\疾病\\" + self.jibing_name + "\\2.html"
        zhengzhuang = open(file_path, 'r', encoding='utf-8').read()
        tree = etree.HTML(zhengzhuang)
        self.jibing_dict['发病原因'] = tree.xpath("//p[@class='spea']/text()") + tree.xpath("//p[@style='text-indent:2em']/text()")

    def yufang_parse(self):
        file_path = "E:\\疾病\\" + self.jibing_name + "\\3.html"
        yufang = open(file_path, 'r', encoding='utf-8').read()
        tree = etree.HTML(yufang)
        self.jibing_dict['预防措施'] = tree.xpath("//p[@class='spea']/text()") + tree.xpath("//p[@style='text-indent:2em']/text()")

    def jiancha_parse(self):
        file_path = "E:\\疾病\\" + self.jibing_name + "\\4.html"
        jiancha  = open(file_path, 'r', encoding='utf-8').read()
        tree = etree.HTML(jiancha)
        jianchaxiangmu = tree.xpath("//a[@style='cursor: default']//text()")
        jianchaneirong = tree.xpath("//p[@class='spea']/text()") + tree.xpath("//p[@style='text-indent:2em']/text()")
        self.jibing_dict['检查项目'] =  jianchaxiangmu
        self.jibing_dict['检查内容'] = jianchaneirong

    def jianbie_parse(self):
        file_path = "E:\\疾病\\" + self.jibing_name + "\\5.html"
        jianbie  = open(file_path, 'r', encoding='utf-8').read()
        tree = etree.HTML(jianbie)
        jianbieneirong = tree.xpath("//p[@class='spea']/text()") + tree.xpath("//p[@style='text-indent:2em']/text()")
        self.jibing_dict['鉴别'] =  jianbieneirong

    def zhiliao_parse(self):
        file_path = "E:\\疾病\\" + self.jibing_name + "\\6.html"
        zhiliao  = open(file_path, 'r', encoding='utf-8').read()
        tree = etree.HTML(zhiliao)
        self.jibing_dict['治疗'] = tree.xpath("//p[@class='spea']/text()") + tree.xpath("//p[@style='text-indent:2em']/text()")

    def huli_parse(self):
        file_path = "E:\\疾病\\" + self.jibing_name + "\\7.html"
        huli  = open(file_path, 'r', encoding='utf-8').read()
        tree = etree.HTML(huli)
        self.jibing_dict['护理'] = tree.xpath("//p[@class='spea']/text()") + tree.xpath("//p[@style='text-indent:2em']/text()")

    def bingfazheng_parse(self):
        file_path = "E:\\疾病\\" + self.jibing_name + "\\8.html"
        bingfazheng  = open(file_path, 'r', encoding='utf-8').read()
        tree = etree.HTML(bingfazheng)
        self.jibing_dict['并发症'] = tree.xpath("//p[@class='spea']/text()") + tree.xpath("//p[@style='text-indent:2em']/text()")


if __name__ =='__main__':
    start_time = time.time()
    rootdir = 'E:\\疾病'
    mongoClient = MongoClient('localhost', 27017)
    datadb = mongoClient.healthPedia
    illness = datadb['illness']
    error_collection = open("E:\\error.txt",'a',encoding='utf-8')
    for parent, dirnames, filenames in os.walk(rootdir):
        for dirname in dirnames:
            try:
                print("开始解析疾病:  " + dirname)
                parser = jibing_parse(dirname)
                parser.jianjie_parse()
                parser.zhengzhuang_parse()
                parser.yufang_parse()
                parser.bingyin_parse()
                parser.jiancha_parse()
                parser.jianbie_parse()
                parser.zhiliao_parse()
                parser.huli_parse()
                parser.bingfazheng_parse()
                illness.insert(parser.jibing_dict)
                # print("成功写入MongoDB")
            except:
                error_collection.write(dirname+'\n')



    end_time = time.time()
    print("一共花了  "+str(end_time-start_time)+" 时间")






