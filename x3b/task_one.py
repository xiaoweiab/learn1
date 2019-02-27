import json
import os
import re


def count_profit(json_content):
    project = json_content['data']['主营构成-按项目名称展示']
    profit_dict = dict()
    profit_dict.__setitem__('2013年年报', 0)
    profit_dict.__setitem__('2013年中报', 0)
    profit_dict.__setitem__('2014年年报', 0)
    profit_dict.__setitem__('2014年中报', 0)
    profit_dict.__setitem__('2015年年报', 0)
    profit_dict.__setitem__('2015年中报', 0)
    profit_dict.__setitem__('2016年年报', 0)
    profit_dict.__setitem__('2016年中报', 0)

    if project :
        for key in project:
            profits = project[key]['营业利润(元)']
            # print(key+str(profits))
            try:
                for time in profits:
                    if profits[time] is not None:
                        profit_dict[time] = profit_dict[time] + profits[time]
            except:
                pass
        return profit_dict
        # print("all money "+str(profit_dict))
        # print()
        # print()
    else:
        print("no project")
    return profit_dict
#
def task_one(json_content,file_name,file_task_one):
    company_name = file_name.replace('.json','')

    data = json_content['data']
    leaders = data['leaders']
    supervisorList = leaders['supervisorList']
    managerList = leaders['managerList']
    directorList = leaders['directorList']

    holder_dict = None
    try:
        holder = data['holder']['topten']
        # print(holder)
        time_list = ['2016-12-31', '2016-06-30', '2015-12-31', '2015-06-30', '2014-12-31', '2014-06-30']
        for time in time_list:
            try :
                # print("--------------------------------------------------------")
                holder_dict = holder[time]
                break
            except:
                pass
    except:
        print("not holder")


    leader_list = supervisorList+managerList+directorList

    for supervisor in leader_list:
        name = supervisor['姓名']
        positiion = supervisor['职务']
        birth = supervisor['出生日期']
        education = supervisor['学历']
        resume = supervisor['简历']


        # 性别
        sex = ""
        try:
            if '男' in resume or '先生' in resume:
                sex = "男"
            else:
                sex = '女'
        except:
            sex = 'null'

        # 学校
        school = ''
        try:
            pattern = re.compile(r'.*毕业于(.*?(学院|大学|中学))[.。；，/].*')  # 查找数字
            school_pattern = pattern.findall(resume)
            if school_pattern:
                school , school_2 = school_pattern[0]
            else:
                school = "null"
        except:
            school = 'null'

        # 国籍
        country = ''
        try:
            country_pattern = re.compile(r'，(\w{1,3})国籍[.。；，/].*')  # 查找数字
            country_pattern = country_pattern.findall(resume)
            if country_pattern:
                country = country_pattern[0]
                if country == '中':
                    country='中国'
            else:
                country = "null"
        except:
            country = 'null'

        # 持股比例
        if holder_dict is None:
            holder_share = 0
        else:
            try:
                holder_share = holder_dict[name]['占总股本比例(%)']
                # print(name+" "+str(holder_share['占总股本比例(%)']))
            except:
                holder_share = 0


        #  营收数据
        profit = count_profit(json_content)

        string_task1 = "{}#{}#{}#{}#{}#{}#{}#{}#{}#{} {}".format(
            name,sex,country,education,birth,str(holder_share),positiion,school,str(profit),company_name,'\n'
        )
        # print(string_task1)
        try:
            file_task_one.write(string_task1)
        except:
            pass
    # return string_task1


if __name__ == '__main__':
    base_path = 'E:\\知识图谱实验室\\数据集\\新三板\\x3b'

    path = 'C:\\Users\\Hasee\\Desktop\\新三板整理数据\\task1.txt'
    file_task_one = open(path, 'a', encoding='utf-8')
    str_title = "{}#{}#{}#{}#{}#{}#{}#{}#{}#{} {}".format(
        '高管姓名','性别','国籍','学历','出生日期',
        '持股比例','职务','毕业学校','营业利润','公司名字','\n'

    )
    file_task_one.write(str_title)

    for i, file_name in enumerate(os.listdir(base_path)):
        print(i)
        file_path = base_path + '\\' + file_name
        file = open(file_path, 'r', encoding='utf-8')
        json_content = json.load(file)
        task_one(json_content,file_name,file_task_one)
        # break

    print("ok")


