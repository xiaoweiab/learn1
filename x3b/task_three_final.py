import os
import json



def main(json_content,address_dict,file_name):

    main_company_name = file_name.replace('.json','')
    data = json_content['data']

    sub_company_report = data['控股参股子公司']
    try:
        for report in sub_company_report:
            address_count = {}
            for company in sub_company_report[report]:
                company_address = company['注册地']
                for item in addres_list:
                    if item in company_address:
                        company_address = item
                    else:
                        pass
                try:
                    address_count[company_address] = address_count[company_address] + 1
                except:
                    address_count[company_address] = 1
            # print(report + " " + str(address_count))
            for k, v in address_count.items():
                print("{}@{}@{}@{}@".format(main_company_name,report,k,v))
    except :
        pass



if __name__ == '__main__':

    base_path = 'E:\\知识图谱实验室\\数据集\\新三板\\x3b'

    address_file = open('地区.txt','r',encoding='utf-8').read()
    addres_list  = address_file.split('\n')[:-1]


    for i, file_name in enumerate(os.listdir(base_path)):
        # print(i)
        file_path = base_path + '\\' + file_name
        file = open(file_path, 'r', encoding='utf-8')
        json_content = json.load(file)
        avg_profit = count_profit(json_content)
        if avg_profit:
           main(json_content, addres_list, file_name)
    print("ok")