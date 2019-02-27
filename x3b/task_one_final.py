import os
import json
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
        values = list(profit_dict.values())
        sum = 0
        count = 0
        for value in values:
            if value == 0 :
                pass
            else:
                sum = sum +value
                count = count + 1
        if count ==0 :
           avg = 0
        else:
           avg = sum / count
        # print(values)
        # print(sum)
        # print(count)
        # print(avg)
        return  avg

    else:
        print("no project")
        return None




def main(json_content):
    company_name = file_name.replace('.json', '')+"@"

    data = json_content['data']
    leaders = data['leaders']
    supervisorList = leaders['supervisorList']
    managerList = leaders['managerList']
    directorList = leaders['directorList']

    holder_dict = None
    try:
        holder = data['holder']['topten']
        time_list = ['2016-12-31', '2016-06-30', '2015-12-31', '2015-06-30', '2014-12-31', '2014-06-30']
        for time in time_list:
            try:
               holder_dict = holder[time]
               break
            except:
               pass
    except:
        print("not holder")

    leader_list = supervisorList + managerList + directorList

    sex_list = []
    age_list = []
    education_list = []
    holder_share_list = []
    for supervisor in leader_list:
            name = supervisor['姓名']
            # positiion = supervisor['职务']

            # 统计年龄
            try:
                birth = supervisor['出生日期'][:4]
                age = 2018-int(birth)
                age_list.append(age)
            except:
                pass

            # 统计学历
            education = supervisor['学历']
            education_list.append(education)


            # 性别
            resume = supervisor['简历']
            try:
                if '男' in resume or '先生' in resume:
                    sex = "男"
                else:
                    sex = '女'
            except:
                sex = 'null'
            sex_list.append(sex)

            # # 学校
            # school = ''
            # try:
            #     pattern = re.compile(r'.*毕业于(.*?(学院|大学|中学))[.。；，/].*')  # 查找数字
            #     school_pattern = pattern.findall(resume)
            #     if school_pattern:
            #         school, school_2 = school_pattern[0]
            #     else:
            #         school = "null"
            # except:
            #     school = 'null'

            # 统计持股比例
            if holder_dict is None:
                holder_share = 0
            else:
                try:
                    holder_share = holder_dict[name]['占总股本比例(%)']
                    # print(name+" "+str(holder_share['占总股本比例(%)']))
                except:
                    holder_share = 0
            holder_share_list.append(holder_share)

    # 统计性别
    sex_list_len = len(sex_list)
    if sex_list_len == 0:
        man_porpotion = 0
        female_porpotion = 0
    else:
        man_porpotion = float(sex_list.count('男'))/sex_list_len
        female_porpotion = 1-man_porpotion
    sex_porpotion_result = '{:.2f}@{:.2}@'.format(float(man_porpotion),float(female_porpotion))

    # 统计平均年龄
    if len(age_list) == 0:
        avg_age = 0

    else:
        avg_age = sum(age_list) / len(age_list)
    avg_age_result = '{:.2f}@'.format(avg_age)

    # 统计统计教育比例
    education_list_len = len(education_list)
    if education_list_len == 0:
       undergraduate =0
       master = 0
       doctor = 0
       lowerundergraduate = 0
    else:
        undergraduate = education_list.count('本科') / education_list_len
        master = education_list.count('硕士') / education_list_len
        doctor = education_list.count('博士') / education_list_len
        lowerundergraduate = 1 - master - undergraduate-doctor
    education_result = '{:.2f}@{:.2}@{:.2f}@{:.2}@'.format(float(undergraduate),float(master),float(doctor),float(lowerundergraduate))
    # 统计平均持股
    holder_share_list_len =  len(holder_share_list)
    if holder_share_list_len == 0:
        holder_share_result = 0
    else:
        holder_share_result = sum(holder_share_list) / holder_share_list_len
    holder_share_result = '{:.2f}@'.format(holder_share_result)

    result = company_name+sex_porpotion_result+avg_age_result+education_result+holder_share_result
    result.replace('\n','')
    return result



if __name__ == '__main__':

    base_path = 'E:\\知识图谱实验室\\数据集\\新三板\\x3b'

    path = 'C:\\Users\\Hasee\\Desktop\\新三板整理数据\\task1.txt'
    file_task_one = open(path, 'a', encoding='utf-8')
    str_title = "{}@{}@ {}@{}@ {}@{}@ {}@{}@ {}@{}".format(
        '公司名字','男性比例','女性比例','平均年龄','本科比例','硕士比例',
        '博士比例','平均持股','营业利润','\n'
    )
    file_task_one.write(str_title)

    for i, file_name in enumerate(os.listdir(base_path)):
        print(i)
        file_path = base_path + '\\' + file_name
        file = open(file_path, 'r', encoding='utf-8')
        json_content = json.load(file)
        avg_profit = count_profit(json_content)
        if avg_profit:
           result =  main(json_content) +str(avg_profit)+'\n'
           file_task_one.write(result)
    print("ok")

