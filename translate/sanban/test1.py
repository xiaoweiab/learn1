import requests
import os

name_list = os.listdir('E:\\新三板\\x3b')
name_dict = dict()
for name in name_list[:-1]:
    code = name.split('_')[0]
    newname = name.replace('.json','_事件.json')
    # print(newname)
    name_dict.__setitem__(code,newname)

# base_path = 'E:\\新三板\\test_rename'
base_path = 'E:\\新三板\\event'
to_rename_list = os.listdir(base_path)
for name in to_rename_list:
    old_file_path = base_path+"\\"+name
    # print(old_file_path)
    new_name = name_dict.get(name.replace('.json',''))
    new_file_path = base_path + "\\" + new_name
    # print(new_file_path)
    os.renames(old_file_path,new_file_path)
print("ok")

