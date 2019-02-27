import requests
from  bs4 import BeautifulSoup
import time
response = requests.get("http://zh.vietnamplus.vn/")
soup = BeautifulSoup(response.text,"lxml")
classgroup = soup.find('nav',id="navigation").find_all('a')
for ul in classgroup:
   href = ul['href']
   class_name = ul.get_text()
   print("开始爬取 "+class_name)
   eng_class = href.replace('.vnp','')
   response1 = requests.get("http://zh.vietnamplus.vn"+href)
   list=BeautifulSoup(response1.text,"lxml").find('span',id="ctl00_mainContent_ctl00_ContentList1_pager").find_all('a')
   page_num=list[-1].get_text()
   for i in range(1,int(page_num)):
       print("爬取第 " +str(i)+" 页")
       link = "http://zh.vietnamplus.vn/"+eng_class+"/page"+str(i)+".vnp"
       response2 = requests.get(link)
       article_list =BeautifulSoup(response2.text,"lxml").find('div',class_="story-listing slist-03").find_all('article')
       for article in article_list:
           print("爬取文章" )
           article_a = "http://zh.vietnamplus.vn"+article.find('a')['href']
           response3 = requests.get(article_a)
           article_content = BeautifulSoup(response3.text,"lxml").find('article',class_="article")
           title = article_content.find('h1').get_text()
           author = article_content.find('span',class_="author").get_text()
           article_time = article_content.find('time').get_text()
           con = article_content.find('div',class_="article-contents").get_text().rstrip()
           print(time.ctime())
           print(title)
           print(article_time)
           print(author)
           print(con)
           print("------------------------------------------------------")