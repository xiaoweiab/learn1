import json
import os


def extract_company_leader(file_name):
    file_path = "E:\\知识图谱实验室\\数据集\\新三板\\x3b\\"+file_name
    # print(file_path)
    json_file = open(file_path,'r',encoding='utf-8')
    json_data = json.load(json_file)
    leader_info = json_data['data']['leaders']
    return leader_info

def extract_history_increase(file_name):
    file_name = file_name.replace('.json','_事件.json')
    file_path1 = "E:\\知识图谱实验室\\数据集\\新三板\\event\\{}".format(file_name)
    json_file = open(file_path1, 'r', encoding='utf-8')
    json_data = json_file.read()
    json_data = eval(json_data)
    history_increase_info = json_data['历史定增']
    return history_increase_info

if __name__ == '__main__':

    file_name_list = os.listdir('E:\\知识图谱实验室\\数据集\\新三板\\x3b')
    for file_name in file_name_list:
        new_file_name = file_name.replace('.json','_公司领导_历史定增.json')
        new_file_path = "E:\\知识图谱实验室\\数据集\\新三板\\公司领导_历史定增\\{}".format(file_name)
        if os.path.exists(new_file_path):
            print("exist")
        else:
            new_file = open(new_file_path, 'w')
            comany_dict = dict()
            detail = dict()
            leader_info = extract_company_leader(file_name)
            history_increase_info = extract_history_increase(file_name)
            detail.__setitem__("公司领导", leader_info)
            detail.__setitem__("历史定增",history_increase_info)
            comany_dict.__setitem__("data",detail)
            new_file.write(json.dumps(comany_dict,ensure_ascii=False,indent=4))


