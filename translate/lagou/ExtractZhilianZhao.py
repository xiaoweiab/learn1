from bs4 import BeautifulSoup
import os
import xlwt
import time
from pymongo import MongoClient


client = MongoClient('60.205.229.245', 27007)
db = client['zhiLian']
job = db['job']


def parse_file(file_name):
    job_dict = dict()
    file_id = file_name.replace('.html','')
    file_path = "C:\\Users\\15708\\Desktop\\知识图谱实验室\\智联招聘\\网页数据\\"+file_name
    file = open(file_path,'r',encoding='utf-8').read()
    # print(file)
    soup = BeautifulSoup(file,"lxml")
    part1 = soup.find('div',class_="inner-left fl")
    postion_name = part1.find('h1').get_text()
    position_fuli = str(part1.find_all('span')).replace('[','').replace(',','').replace(']','')
    # print(postion_name)
    # print(position_fuli)

    job_dict.__setitem__('jobId',file_id)
    job_dict.__setitem__('postionName', postion_name)
    job_dict.__setitem__('positionFuli', position_fuli)

    part2 = soup.find('ul',class_="terminal-ul clearfix")
    # print(part2)
    all_strong = part2.find_all('strong')
    zhiweiyuexin = all_strong[0].get_text()
    gongzuodidian = all_strong[1].get_text()
    faburiqi = all_strong[2].get_text()
    gongzuoxingzhi = all_strong[3].get_text()
    gongzuojingyan = all_strong[4].get_text()
    zuidixueli = all_strong[5].get_text()
    zhaopinrenshu = all_strong[6].get_text()
    zhiyeleibie = all_strong[7].get_text()
    # print(zhiweiyuexin)
    # print(gongzuodidian)
    # print(faburiqi)
    # print(gongzuoxingzhi)
    # print(gongzuojingyan)
    # print(zuidixueli)
    # print(zhaopinrenshu)
    # print(zhiyeleibie)
    job_dict.__setitem__('zhiWeiYueXin', zhiweiyuexin)
    job_dict.__setitem__('gongZuoDiDian', gongzuodidian)
    job_dict.__setitem__('faBuRiQi', faburiqi)
    job_dict.__setitem__('gongZuoXingZhi', gongzuoxingzhi)
    job_dict.__setitem__('gongZuoJingYan', gongzuojingyan)
    job_dict.__setitem__('zuiDiXueLi', zuidixueli)
    job_dict.__setitem__('zhaoPinRenShu', zhaopinrenshu)
    job_dict.__setitem__('zhiYeLeiBie', zhiyeleibie)

    part3= soup.find('div',class_="company-box")
    company_name = part3.find('p',class_="company-name-t").get_text()
    # print(company_name)
    all_strong_part3 = part3.find_all('strong')
    company_guimo = all_strong_part3[0].get_text()
    company_xingzhi = all_strong_part3[1].get_text()
    company_hangye= all_strong_part3[2].get_text()
    company_zhuye = all_strong_part3[3].get_text()
    # print(company_guimo)
    # print(company_xingzhi)
    # print(company_hangye)
    # print(company_zhuye)
    job_dict.__setitem__('companyGuimo', company_guimo)
    job_dict.__setitem__('companyXingzhi', company_xingzhi )
    job_dict.__setitem__('companyHangye', company_hangye)
    job_dict.__setitem__('companyZhuye', company_zhuye)

    part4 = soup.find('div',class_="terminalpage-main clearfix")
    part4s = part4.find_all('div', class_="tab-inner-cont")
    zhiweimiaoshu = str(part4s[0].find_all('p')[:-1]).replace("\"",'')
    gongsijieshao = part4s[1].get_text().replace("\"",'')
    # print(zhiweimiaoshu)
    # print(gongsijieshao)
    job_dict.__setitem__('zhiWeiMiaoShu', zhiweimiaoshu)
    job_dict.__setitem__('gongSiJieShao', gongsijieshao)
    return job_dict





if __name__ == '__main__':


    error_txt_path =  "C:\\Users\\15708\\Desktop\\知识图谱实验室\\智联招聘\\error1.txt"
    error_txt = open(error_txt_path,'a',encoding='utf-8')

    time1= time.time()
    diretory = "C:\\Users\\15708\\Desktop\\知识图谱实验室\\智联招聘\\网页数据"
    file_list = os.listdir(diretory)
    num = 1
    successful_num = 1
    for file in file_list:
        try:
            job_dict1 = parse_file(file)
            job.insert_one(job_dict1)
            successful_num =successful_num +1
            if successful_num % 100 == 0:
                print("成功将"+str(successful_num)+"条记录写入MONGODB")


        except:
            error_txt.write(file+"\n")
        num= num+1





