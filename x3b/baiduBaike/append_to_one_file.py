import os

file_list_path = 'E:\知识图谱实验室\数据集\百度电影简介'
file_list = os.listdir(file_list_path)
out_put_file = open('百度电影简介.txt','a',encoding='utf-8')
for i , file_name in enumerate(file_list):
    name = file_name.replace('.txt','').replace('\n','')
    file_path = file_list_path +"\\"+file_name
    file = open(file_path,'r',encoding='utf-8')
    content = file.read().replace('\n','')
    out_put_string = '{}@{}  \n'.format(name,content)
    out_put_file.write(out_put_string)
    print(i)


