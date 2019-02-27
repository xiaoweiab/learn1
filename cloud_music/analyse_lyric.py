from jieba import analyse
import os

rootdir = 'E:\yunyinyue\歌手\周杰伦'
content  = ""
list = os.listdir(rootdir) #列出文件夹下所有的目录与文件

for i in range(0,len(list)):
      # num = num +1
      path = os.path.join(rootdir,list[i])
      # print(path)
      if os.path.isfile(path):
          file = open(path,'r',encoding='utf-8')
          content = content+file.read()
          file.close()
          # print(content)
          # print(str(num)+"
print(content.replace(' ',''))

analyse.set_stop_words('E:\\yunyinyue\\停用词.txt')
tags = analyse.extract_tags(content,topK=100,withWeight=True)
for tag,n in tags:

    if(tag == '周杰伦'):
        continue
    elif(tag == '作词'):
        continue
    else:
        print(tag + " " + str(int(n * 10000)))

print("分析完成")
