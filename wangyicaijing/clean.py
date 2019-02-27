from bs4 import BeautifulSoup

file = open('C:\\Users\\Administrator\\Desktop\\clean.txt','r',encoding='utf-8')
file1 = open('C:\\Users\\Administrator\\Desktop\\clean2.txt','a',encoding='utf-8')
soup = BeautifulSoup(file.readline(),"lxml")
# li = soup.find('tr')
# for tr in li:
#     data1 = tr.get_text()
#     file1.write(data1+"，")
list = soup.find_all('tr')
for tr in list:
    list1 = tr.find_all('td')
    for td in list1:
        data = td.get_text()
        file1.write(data+"，")
    file1.write("\n")
print("over")