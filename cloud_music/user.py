from selenium import webdriver
from multiprocessing import Pool
import os
from bs4 import BeautifulSoup
import time

class GetUserInformation():
    province = ""
    city = ""
    driver = webdriver.PhantomJS()

    # def __init__(self,url):
    #    url = url

    def get_resoure(slef,url):
        slef.driver.get(url)
        slef.driver.switch_to.frame(slef.driver.find_element_by_xpath("//iframe"))
        content = slef.driver.page_source
        return content

    def get_basic_information(self,content):
        soup = BeautifulSoup(content,"lxml")
        name = soup.find('span',class_="tit f-ff2 s-fc0 f-thide").get_text()
        level = soup.find('span',class_="lev u-lev u-icn2 u-icn2-lev").get_text()
        count_event = soup.find('strong',id="event_count").get_text()
        follow_count = soup.find('strong',id="follow_count").get_text()
        fan_count = soup.find('strong',id="follow_count").get_text()
        address = soup.find('div',class_="inf s-fc3").get_text()
        time.sleep(3)
        rank_list_url =soup.find('div',class_="more")
        like_list_url =soup.find('p',class_="dec")
        print(name)
        print(level)
        print(count_event)
        print(follow_count)
        print(fan_count)
        print(address)
        print(rank_list_url)
        print(like_list_url)

if __name__ =='__main__':
    user = GetUserInformation()
    content= user.get_resoure('http://music.163.com/#/user/home?id=305577682')
    user.get_basic_information(content)


