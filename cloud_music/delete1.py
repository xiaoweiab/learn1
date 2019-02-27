import re
import os
import os.path

lists = ['安静','放松','感动','孤独','怀旧','快乐','浪漫','清新','思念','思念','兴奋','性感','治愈']
all_text_name = []
for list in lists:
    rootdir ="E:\\yunyinyue - 已处理\\train1\\"+list
# rootdir='E:\\yunyinyue\\train\\清新'
    for filenames in os.walk(rootdir):
        allfile = filenames[2]
        for file in allfile:
            all_text_name.append(file)

num = len(all_text_name)
print("num = "+str(num))

lista = []
for text_name in all_text_name:
    appear_num = all_text_name.count(text_name)
    if appear_num>1:
#        print("the "+text_name+" has found "+str(appear_num))
       lista.append(text_name)
print(len(lista))
mylista = set(lista)
print(len(mylista))
# for my in mylista:
    # print(my)
   # file_name = "E:\\yunyinyue - 已处理\\train1\\same.txt"
   # same_text_file = open(file_name,'a',encoding='utf-8')
   # same_text_file.write(my+"\n")
   # same_text_file.close()

lists = ['安静','放松','感动','孤独','怀旧','快乐','浪漫','清新','思念','思念','兴奋','性感','治愈']
all_text_name = []
for list in lists:
    rootdir ="E:\\yunyinyue - 已处理\\train1\\"+list
# rootdir='E:\\yunyinyue\\train\\清新'
    for filenames in os.walk(rootdir):
        allfile = filenames[2]
        for file in allfile:
            filepath = rootdir + "\\" + file
            if file in mylista:
                os.remove(filepath)
    print(list+"删除完成")

