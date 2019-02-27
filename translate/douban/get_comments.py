import os
import requests
from lxml import etree
import time
import json,re
import random
from douban.download import request_own

headers= {

'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'bid=oG4x2BVeDTs; ps=y; dbcl2="172970704:mpWPn6eSRDg"; ll="118281"; ck=9peY; '
         '_pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1516652167%2C%22https%3A%2F%2Faccounts.douban.com%2Flogin%3Fredir%3Dhttps%3A%2F%2Fmovie.douban.com%2Fsubject%2F6874741%2F%3Ffrom%3Dshowing%26source%3DNone%26login_type%3Dsms%22%5D; '
         '_pk_ses.100001.4cf6=*; __utma=30149280.1996786522.1516652167.1516652167.1516652167.1; '
         '__utmb=30149280.0.10.1516652167; __utmc=30149280; '
         '__utmz=30149280.1516652167.1.1.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/login; '
         '__utma=223695111.1102124544.1516652167.1516652167.1516652167.1; __utmb=223695111.0.10.1516652167; '
         '__utmc=223695111; __utmz=223695111.1516652167.1.1.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/login; '
         'push_noty_num=0; push_doumail_num=0; _vwo_uuid_v2=70468E827AF4A23FFC8AF162D8215536|f1e39d4bf31aba6012bb046131147e2c; '
         '_pk_id.100001.4cf6=4c52443f5f48def0.1516652167.1.1516652178.1516652167.',
'Host':'movie.douban.com',
'Referer':'https://movie.douban.com/subject/6874741/?from=showing',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
# time_list = [0.1,0.15,0.2,0.25,0.3,0.35,0.4]

def get_comment_page(movie_link):
    headers['Referer'] = movie_link+"/?from=showing"
    movie_comment_list = list()
    base_url = movie_link+"/comments?start=page&limit=20&sort=new_score&status=P"
    for i in range(0,20):
        url = base_url.replace('page',str(i*20))
        # response = request_own.get(url=url,headers=headers).text
        # print(response)
        try:
            response = requests.get(url=url,headers=headers).text
            # print(response)
            time.sleep(0.5)
        except:
            time.sleep(3)
            print("访问出错，休眠3秒后，重新访问")
            response = requests.get(url=url,headers=headers).text
        comment_list = parse_comment(response)
        movie_comment_list = movie_comment_list+comment_list
    return movie_comment_list


def parse_comment(response):

    tree = etree.HTML(response)
    comment_item_list = tree.xpath('//*[@id="comments"]/div[@class="comment-item"]')
    comment_list = list()
    for comment_item in comment_item_list:
        comment_item_dict = dict()
        comment_people  = comment_item.xpath('.//div[2]/h3/span[2]/a/text()')
        vote  = comment_item.xpath('.//div[2]/h3/span[1]/span/text()')
        time  = comment_item.xpath('.//div[2]/h3/span[2]/span[3]/@title')
        comment_content = comment_item.xpath('.//div[2]/p/text()')
        comment_item_dict.__setitem__("评论人",comment_people)
        comment_item_dict.__setitem__("评论有用数量",vote)
        comment_item_dict.__setitem__("评论时间", time)
        comment_item_dict.__setitem__("评论内容", comment_content)
        comment_list.append(comment_item_dict)
    return comment_list

if __name__ == '__main__':

    movie_file = open("E:\\知识图谱实验室\\数据集\\豆瓣电影\\sample.csv",'r')
    for line in movie_file:
        line_list = line.split(';')
        movie_name = line_list[0]
        movie_name = re.sub('[\/:*?"<>|]', '', movie_name)
        movie_comment_file_path = "E:\\知识图谱实验室\\数据集\\豆瓣电影\\影评\\"+movie_name+".json"
        if os.path.exists(movie_comment_file_path):
            print(movie_name + "  ： 已存在")
        else:
            movie_link = line_list[1].replace('\n','').replace("\"",'')
            movie_comment_list =get_comment_page(movie_link)
            movie_comment_file = open(movie_comment_file_path, 'w', encoding='utf-8')
            movie_comment_file.write(json.dumps(movie_comment_list, ensure_ascii=False, indent=4))
            print(movie_name+"  ： 成功爬取")




