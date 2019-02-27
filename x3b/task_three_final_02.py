import os
import json
from zone.zone_province_city import query_zone

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

def main(json_content):

    data = json_content['data']

    sub_company_report = data['控股参股子公司']
    company_address_list  = []
    try:
        for report in sub_company_report:
            companys = sub_company_report[report]
            for company in companys:
                company_address = company['注册地']
                company_address_list.append(company_address)
    except:
        pass

    zone_count_dict = {
        '东北' : 0,
        '华东' : 0,
        '华北' : 0,
        '华中' : 0,
        '华南' : 0,
        '西南' : 0,
        '西北' : 0,
        '其他' : 0,
    }

    if company_address_list:
        for company_address in company_address_list:
            company_address = company_address.replace('全国','')
            # print(company_address)
            zone_dict = query_zone(address=company_address)
            if zone_dict:
                zone = zone_dict['zone']
                zone_count_dict[zone] = zone_count_dict[zone] + 1
            else:
                zone_count_dict['其他'] = zone_count_dict['其他'] + 1
                # print("can't find zone")
        return zone_count_dict
    else:
        return None





if __name__ == '__main__':

    base_path = 'E:\\知识图谱实验室\\数据集\\新三板\\x3b'

    path = 'C:\\Users\\Hasee\\Desktop\\新三板整理数据\\task3_final_02.txt'
    file_task_3 = open(path, 'a', encoding='utf-8')

    for i, file_name in enumerate(os.listdir(base_path)):
        print(i)
        file_path = base_path + '\\' + file_name
        file = open(file_path, 'r', encoding='utf-8')
        json_content = json.load(file)
        avg_profit = count_profit(json_content)
        if avg_profit:

            result =  main(json_content)
            if result :
                main_company_name = file_name.replace('.json', '')
                result_string = '{}@{} \n'.format(main_company_name,result)
                file_task_3.write(result_string)
    print("ok")