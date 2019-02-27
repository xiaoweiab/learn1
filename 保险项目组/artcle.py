import requests
import os

num = 0
file1 = open('E:\\保险项目组\\保险.txt','r',encoding='utf-8')
file2  = open('E:\\保险项目组\\文章\\失败链接.txt','a',encoding='utf-8')
for line in file1:
    all = line.split()
    title = all[0]
    link = all[1]
    title = title.replace('?', '').replace('！', '').replace('|', '｜')
    print(title)
    if 'articleId' in link:
        path = "E:\\保险项目组\\文章\\article\\" + title + ".html"
    elif 'taskid' in link:
        path = "E:\\保险项目组\\文章\\task\\" + title + ".html"
    elif 'formId' in link:
        path = "E:\\保险项目组\\文章\\form\\" + title + ".html"
    else:
        path = "E:\\保险项目组\\文章\\else\\" + title + ".html"

    if os.path.exists(path):
        path = path.replace('.html', '(1).html')
    num = num + 1
    try:
        response = requests.get(link)
        # print(response.text)
        file = open(path, 'w', encoding='utf-8')
        file.write(response.text)
        print("第 " + str(num) + " 个网页下载完成 ")


    # if num == 10:
    #   break
    except:
        print("第 " + str(num) + " 个网页下载失败 ")
        file2.write(link + "\n")


