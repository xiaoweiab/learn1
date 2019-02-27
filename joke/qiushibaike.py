import requests
from bs4 import BeautifulSoup
import lxml
import time
num= 0
for i in range(1,36):
   url = "https://www.qiushibaike.com/text/page/"+str(i)
   response = requests.get(url)
   time.sleep(3)
   soup = BeautifulSoup(response.text,"lxml")
   print("正打印第"+str(i)+"页")
   all_content = soup.find_all('div',class_="article block untagged mb15")
   for content in all_content:
      num = num + 1
    # print(content)
      author = content.find('h2').get_text()
      con = content.find('div', class_="content").get_text().rstrip().lstrip()
      fun = content.find('span',class_="stats-vote").find('i').get_text()
      # comment = content.find('span',class_="stats-comments").get_text()



print(num)