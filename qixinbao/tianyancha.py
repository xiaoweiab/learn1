import random
import requests
from multiprocessing import Pool
import time
from requests.exceptions import ConnectionError


def get_link():
    list = []
    path1 = 'E:\provider\companys .txt'
    file = open(path1,'r')
    for line in file:
       company_name = line.split()[0]
       link = "http://www.tianyancha.com/v2/search/"+company_name+".json?"
       list.append(link)

    return list

def get_data(link):
   try:
       user_agent_list = [
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
           "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
           "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
           "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
           "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
           "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
           "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
           "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
           "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
       ]
       UA = random.choice(user_agent_list)
       headers = {'User-Agent': UA}
       response = requests.get(link,headers=headers)

       return response
   except TimeoutError:
       get_data(link)


def parse(response):

    if len(response.text)>130:

       file1 = open("E:\provider\\天眼查数据\\总表1.txt", 'a', encoding='utf-8')
       file1.write(str(response.text) + '\n')
       # json1 = json.loads(response.text).get('data')
       # for item in json1:
       #     print(item)
    else:
        file1 = open("E:\\provider\\天眼查数据\\error2.txt", 'a')
        file1.write(response.url+'\n')


if __name__ == '__main__':
    links = get_link()
    print(len(links))
    for i in range(0,240):

        print("开始获取数据 "+str(i*200+1)+"个企业信息")
        pool = Pool(2)
        start = time.time()
        begin_num = i*200
        if begin_num == 240:
            end_num = 47964
        end_num = begin_num+200
        contents = pool.map(get_data,links[begin_num:end_num])
        time.sleep(0.05)
        pool.close()
        pool.join()

        for content in contents:
           print(content)
           # parse(content)
        end = time.time()
        print("一共耗时" + str(end - start))
        print("已经获取完成")


