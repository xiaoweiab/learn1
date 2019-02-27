import json
import os
from xlrd import open_workbook
from xlutils.copy import copy

base_path = "E:\\知识图谱实验室\\数据集\\新三板\\整理数据初稿\\x3bcq4"

def append_excel(datas):
    rexcel = open_workbook("E:\\知识图谱实验室\\数据集\\新三板\\整理数据初稿\\名称简介.xlsx")
    rows = rexcel.sheets()[0].nrows
    excel = copy(rexcel)
    table = excel.get_sheet(0)
    row = rows
    for data in datas:
        table.write(row, 0, data['shortname'])
        table.write(row, 1, data['公司名称']) # xlwt对象的写方法，参数分别是行、列、值
        row += 1
    excel.save("E:\\知识图谱实验室\\数据集\\新三板\\整理数据初稿\\名称简介.xlsx") # xlwt对象的保存方法，这时便覆盖掉了原来的excel



data_list  = list()
for file_name in os.listdir(base_path):
    file_path = base_path+"\\"+file_name
    file = open(file_path,'r',encoding='utf-8')
    data  = json.load(file)
    data_list.append(data)
    count  = len(data_list)
    if count % 1000 == 0 :
        print(count)
print("load sucessfully")
append_excel(data_list)
print("ok")


