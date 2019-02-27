from bs4 import BeautifulSoup
import re



for i in range(1,2814):
    if i == 340 or i ==2121 :
       i = i  + 1
    print(str(i))
    file_path = "C:\\Users\\15708\\Desktop\\产品页面代码1\\default118.html".replace("118",str(i))
    print(file_path)
    file = open(file_path,'r',encoding='utf-8')
    soup = BeautifulSoup(file,"lxml")
    product_head = soup.find('div', class_="suspend-info")
    product_name = product_head.find('h3')
    print(product_name.get_text())
    recommand_reason = product_head.find_all('p')
    print("推荐理由：")
    for p in recommand_reason:
        print(p.get_text().lstrip().rstrip())
    print("产品保障：")
    try:
        protects = product_head.find('ul', class_="f-oh list").find_all('li')

        for protect in protects:
            print(protect.get_text())
    except:
        print("null")
    print("===============================================================================")



