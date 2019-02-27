from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests

driver = webdriver.PhantomJS()
driver .get("http://neihanshequ.com/")
getmore = driver.find_element_by_id('loadMore')
# for i in range(1,12):
#     getmore.click()
#     time.sleep(1)

page = driver.page_source
# print(page)
contents = BeautifulSoup(page,"lxml").find('ul',id="detail-list").find_all('div',class_="detail-wrapper")
num =0
for content in contents:
    # print(content)
    user_id = content.find('div',class_="header").find('a')['href']
    user_id = user_id.replace('http://neihanshequ.com/user/','').replace('//','')
    user_name = content.find('div',class_="header").find('span',class_="name").get_text()
    time = content.find('div',class_="header").find('span',class_="time")['title']
    print(user_id)
    print(user_name)
    print(time)
    print("=====================================")
    joke_id =content.find('li',class_="share-wrapper right")['data-group-id']
    joke_content = content.find('li',class_="share-wrapper right")['data-text']
    digg_num = content.find('span',class_="digg").get_text()
    bury_num = content.find('span',class_="bury").get_text()
    joke_url = content.find('li', class_="share-wrapper right")['data-url']
    print(joke_id)
    print(joke_content)
    print(digg_num)
    print(bury_num)
    print("=====================================")
    driver.get(joke_url)
    page = driver.page_source
    comment_list = BeautifulSoup(page,"lxml").find_all('li',class_="comment-item")
    for comment in comment_list:
        print(comment)
        comment_user = comment.find('span',class_="name").get_text()
        comment_user_id = content.find('a')['href'].replace('/user/','').replace('/','')
        # comment_time = comment.find('span',class_="time timeago")['title']
        comment_content = comment.find('p',class_="indent").get_text()
        print(comment_user+"  "+comment_user_id+"   "+comment_content)

    print("---------------------------------------------------------------------")
    num = num +1
print(num)
