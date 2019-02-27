import os
import re
from bs4 import BeautifulSoup


def extract_name(soup):
    try:
        content = soup.find('dd',class_="lemmaWgt-lemmaTitle-title")
        name = content.find('h1').get_text()
        return name
    except:
        return None

def extract_type(soup):
    global type_string
    type_string = ''
    base_info  = soup.find_all('div',class_="basic-info cmn-clearfix")
    if base_info:
        info = base_info[0]
        dts = info.find_all('dt')
        dds = info.find_all('dd')
        for i in range(len(dts)):
            dt = dts[i].get_text()
            dt.replace(' ','').replace('\n','')
            dd = dds[i].get_text()
            dd.replace('&nbsp;', '').replace('\n', '')
            if dt == '类    型' :
               type_string = dd
            else:
                pass


    else:
        # print("抽取基本信息出错")
        pass
    return type_string

if __name__ == '__main__':
    path = 'E:\\知识图谱实验室\\数据集\\百度百科电影1\\'
    path1 = 'E:\\知识图谱实验室\\数据集\\百度电影简介\\'
    result_file = open('电影类型.csv','a',encoding='utf-8')
    result_file.write('{}@{} \n'.format('电影名称','电影类型'))
    file_list = os.listdir(path)
    for i, file_name in enumerate(file_list):

        file_path = path + file_name
        file = open(file_path, 'r', encoding='utf-8')
        content = file.read()
        soup = BeautifulSoup(content,"lxml")
        name = extract_name(soup)
        if name  :
               type_result =  extract_type(soup)
               type_result = type_result.replace('\n','')
               result_file.write('{}@{} \n'.format(name,type_result))
        else:
            print(str(i)+"  "+file_name)
        # break