import requests
from lxml import etree




response = requests.get('http://www.zhaotie.com/index.htm')
response.encoding = 'gbk'

etree1 = etree.HTML(response.text)
uls = etree1.xpath('.//div[@class="city_all"]/ul')
province_dict = {}
for ul in uls :
    lis = ul.xpath('.//li')
    print("=========================================")
    province = ul.xpath('.//span/text()')[0]
    province = province.replace('[','').replace(']','')
    province_city = []
    print(province)
    for li in reversed(lis) :

        city = li.xpath('.//a/text()')[0]
        print(city)
        if '更多' in city:
            link = li.xpath('.//a/@href')[0]
            response1 = requests.get(link)
            response1.encoding = 'gbk'
            etree1 = etree.HTML(response1.text)
            province_city = etree1.xpath('.//div[@class="city_all"]/ul/li/a/text()')
            province_dict.__setitem__(province, province_city)
            # print(province_dict)
            break
        else:
            province_city.append(city)
    province_dict.__setitem__(province,province_city)




