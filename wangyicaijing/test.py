import requests
import lxml
import json

url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=200&page_start=0'
response = requests.get(url)
# print(response.json())
# print(response.cookies)
# print(response.content)
# print(response.headers)
list = response.json().get('subjects')
num = 0
for items in list :
    print(items)
    num = num +1
    # for item in items:
    #     print(item+"  "+str(items.get(item)))
print(num)