import json
import os





def task_two(json_content,file_name,file_task_two):

    main_company_name = file_name.replace('.json','')

    data = json_content['data']
    product_detail = data['brief']['主营产品详细']
    address = data['brief']['所属地域']
    profit_dict = count_profit(json_content)
    sub_company_report = data['控股参股子公司']
    try :
        for key in sub_company_report:
            for company in sub_company_report[key]:
                company_name = company['参控公司']
                company_bussness = company['主营业务']
                company_address = company['注册地']
                relation = company['参控关系']
                hold_rate = company['持股比例(%)']
                profit = company['净利润(万元)']
                string_2 = '{}@ {}@ {}@ {}@ {}@ {}@ {}@ {}@ {}@ {}@  {}'.format(
                    main_company_name,product_detail, company_name, key,
                    company_bussness, company_address, address, relation, hold_rate, str(profit_dict), '\n')
                # print(string_2)
                file_task_two.write(string_2)
    except:
        pass


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





if __name__ == '__main__':
    base_path = 'E:\\知识图谱实验室\\数据集\\新三板\\x3b'

    path = 'C:\\Users\\Hasee\\Desktop\\新三板整理数据\\task2.txt'
    file_task_two = open(path, 'a', encoding='utf-8')
    str_title = '{}# {}# {}# {}# {}# {}# {}# {}# {}# {}# {}'.format(
        '主公司名','主公司的主营产品详细', '参控公司名称',
        '报表', '参控公司业务', '注册地',
        '主公司所属地域', '参控关系', '持股比例',
        '利润字典','\n')
    file_task_two.write(str_title.replace('#','@'))

    for i, file_name in enumerate(os.listdir(base_path)):
        print(i)
        file_path = base_path + '\\' + file_name
        file = open(file_path, 'r', encoding='utf-8')
        json_content = json.load(file)
        task_two(json_content,file_name,file_task_two)

    print('ok')
