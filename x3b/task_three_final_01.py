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

def main(json_content,file_name):

    main_company_name = file_name.replace('.json','')
    data = json_content['data']

    sub_company_report = data['控股参股子公司']
    sub_company_dict = {
        '2013中报': 0 ,
        '2013年报': 0 ,
        '2014中报': 0,
        '2014年报': 0,
        '2015中报': 0,
        '2015年报': 0,
        '2016中报': 0,
        '2016年报': 0,
    }
    try:
        for report in sub_company_report:
            company_num = len(sub_company_report[report])
            sub_company_dict.__setitem__(report,company_num)
        result = main_company_name+"@"+str(sub_company_dict)
        return  result+'\n'
    except :
        pass



if __name__ == '__main__':

    base_path = 'E:\\知识图谱实验室\\数据集\\新三板\\x3b'

    # address_file = open('地区.txt','r',encoding='utf-8').read()
    # addres_list  = address_file.split('\n')[:-1]
    path = 'C:\\Users\\Hasee\\Desktop\\新三板整理数据\\task3_final_01.txt'
    file_task_3 = open(path, 'a', encoding='utf-8')

    for i, file_name in enumerate(os.listdir(base_path)):
        print(i)
        file_path = base_path + '\\' + file_name
        file = open(file_path, 'r', encoding='utf-8')
        json_content = json.load(file)
        avg_profit = count_profit(json_content)
        if avg_profit:
            result =  main(json_content, file_name)
            if result:
               file_task_3.write(result)
    print("ok")