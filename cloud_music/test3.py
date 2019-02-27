from selenium import webdriver
from multiprocessing import Process
from multiprocessing import Pool
from lxml import etree
from bs4 import BeautifulSoup
import time
import os

# driver = webdriver.PhantomJS()

driver = webdriver.Firefox()
driver.get("http://music.163.com/#/artist?id=6452")
all_album=driver.find_element_by_css_selector("#m_tabs > li:nth-child(2) > a:nth-child(1) > em:nth-child(1)")
all_album.click()




# if __name__=='__main__':
#
#     # print(content)
#     # parse_lyric(content)
#     # isExists('Black Diamond')