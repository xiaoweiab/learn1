import os
import json


def count_profit(json_content):
    project = json_content['data']['finance']

    if project :
        # print(project)
        try:
            profits = project['基本财务指标']['净资产收益率']
            # print(str(profits))
            values = list(profits.values())
            values_sum = sum(values)
            values_len = len(values)
            if values_len :
                values_avg = values_sum / values_len
            else:
                values_avg = 0
        except:
            values_avg = 0

        return  values_avg

    else:
        print("no project")
        return None

def main(json_content,file_name,address_list):

    company_name = file_name.replace('.json','')
    relation_list = [
        '全资','控股','参股','民营','间接控股'
    ]

    company_num = 0
    city_set = set()
    relation_count = {
        '全资':0  ,
        '控股':0  ,
        '参股':0  ,
        '民营':0  ,
        '间接控股':0,
        '其他':0
    }

    hold_rate_sum = 0

    data = json_content['data']
    sub_company_report = data['控股参股子公司']
    try :
        for report in sub_company_report:
            for company in sub_company_report[report]:

                company_num = company_num + 1

                company_address = company['注册地']
                for item in address_list:
                    if item in company_address:
                       city_set.add(item)
                       break
                    else:
                        pass

                relation = company['参控关系']
                for item in relation_list:

                    if item in relation:
                        relation_count[item] = relation_count[item] +1
                        break
                    elif item == relation[-1]:
                        relation_count['其他'] = relation_count['其他'] + 1
                    else:
                        pass
                hold_rate_sum = hold_rate_sum + company['持股比例(%)']

        for key ,value in relation_count.items() :
            relation_count[key] = value / company_num

        avg_hold_rate = hold_rate_sum / company_num
        result_string = "{}@{}@{}@{}@{}@".format(
            company_name,company_num,len(city_set),avg_hold_rate,relation_count)
        return result_string



    except:
        print("没有参股子公司")
        return None





if __name__ == '__main__':

    address_file = open('地区.txt', 'r', encoding='utf-8').read()
    address_list = address_file.split('\n')[:-1]

    base_path = 'E:\\知识图谱实验室\\数据集\\新三板\\x3b'

    path = 'C:\\Users\\Hasee\\Desktop\\新三板整理数据\\task2_final_01.txt'
    file_task_one = open(path, 'a', encoding='utf-8')
    # str_title = "{}@{}@ {}@{}@ {}@{}@ {}@{}@ {}@{}".format(
    #     '公司名字','男性比例','女性比例','平均年龄','本科比例','硕士比例',
    #     '博士比例','平均持股','营业利润','\n'
    # )
    # file_task_one.write(str_title)

    for i, file_name in enumerate(os.listdir(base_path)):
        print("----------------------------------------------------------------------")
        print(i)

        file_path = base_path + '\\' + file_name
        file = open(file_path, 'r', encoding='utf-8')
        json_content = json.load(file)
        avg_profit = count_profit(json_content)

        if avg_profit:
           result =  main(json_content,file_name,address_list)
           if result :
               result = result +'{:.2f}'.format(avg_profit)+'\n'
               # print(result)
               file_task_one.write(result)
    print("ok")