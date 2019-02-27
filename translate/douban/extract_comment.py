import json
import os
from xlrd import open_workbook
from xlutils.copy import copy


def append_excel(name, datas):
    rexcel = open_workbook("E:\\知识图谱实验室\\数据集\\豆瓣电影\\影评数据2.xlsx")
    rows = rexcel.sheets()[0].nrows
    excel = copy(rexcel)
    table = excel.get_sheet(0)
    row = rows
    for data in datas:
        table.write(row, 0, name)  # xlwt对象的写方法，参数分别是行、列、值
        try:
            table.write(row, 1, data['评论人'][0])
        except BaseException:
            table.write(row, 1, "null")
        try:
            table.write(row, 2, data['评论有用数量'][0])
        except BaseException:
            table.write(row, 2, "null")
        try:
            table.write(row, 3, data['评论时间'][0])
        except BaseException:
            table.write(row, 3, "null")
        try:
            table.write(row, 4, data['评论内容'][0])
        except BaseException:
            table.write(row, 4, "null")
        row += 1
    # xlwt对象的保存方法，这时便覆盖掉了原来的excel
    excel.save("E:\\知识图谱实验室\\数据集\\豆瓣电影\\影评数据2.xlsx")
    print(name)


base_dir = "E:\\知识图谱实验室\\数据集\\豆瓣电影\\影评"
file_list = os.listdir(base_dir)
num = 1
for file_name in file_list:
    # print(file_name)
    file_path = base_dir + "\\" + file_name
    file = open(file_path, 'r', encoding='utf-8')
    datas = json.load(file)
    name = file_name.replace('.json', '')
    num = num + 1
    if num < 300:
        pass
    elif num == 500:
        break
    else:
        append_excel(name, datas)
    # for data in datas :
    #     people = data['评论人'][0]
    #     num = data['评论有用数量'][0]
    #     time = data['评论时间']
    #     content = data['评论内容'][0].replace('\\n','').strip()
    #     print("%s##%s##%s##%s" %(people,num,time,content))
