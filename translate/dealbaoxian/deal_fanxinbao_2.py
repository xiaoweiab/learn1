from lxml import etree
import xlrd
import requests
import os


def parse_product_page(page,link,name,type):
    product_dict = dict()
    product_dict.__setitem__('产品名称', name)
    product_dict.__setitem__('产品链接', link)
    product_dict.__setitem__('产品类别', type)

    tree = etree.HTML(page)

    age = tree.xpath('//div[@class="sing_txt floatleft newCpage"]/table/tbody/tr[2]/td[2]/text()')
    if(len(age)== 0 ):
        product_dict.__setitem__('承保年龄', "none")
    else:
        age = age[0].strip()
        product_dict.__setitem__('承保年龄', age)

    time_limit = tree.xpath('//div[@class="sing_txt floatleft newCpage"]/table/tbody/tr[3]/td[2]/font[@class="f_d84600"]/text()')
    if (len(time_limit) == 0):
        product_dict.__setitem__('保险期限', "none")
    else:
        product_dict.__setitem__('承保年龄',time_limit)

    submit_way = tree.xpath('//div[@class="sing_txt floatleft newCpage"]/table/tbody/tr[4]/td[2]/font[@class="f_d84600"]/text()')
    product_dict.__setitem__('交费方式',submit_way)

    min_money = tree.xpath('//div[@class="sing_txt floatleft newCpage"]/table/tbody/tr[5]/td[2]/font[@class="f_d84600"]/text()')
    product_dict.__setitem__('最低保额', submit_way)
    max_money = tree.xpath('//div[@class="sing_txt floatleft newCpage"]/table/tbody/tr[6]/td[2]/font[@class="f_d84600"]/text()')
    product_dict.__setitem__('最高保额', submit_way)
    return product_dict


if __name__ == '__main__':

    data = xlrd.open_workbook('C:\\Users\\Hasee\\Desktop\\放心保数据\\page.xlsx')
    table = data.sheets()[0]
    nrows = table.nrows

    product_dict_text = open("C:\\Users\\Hasee\\Desktop\\放心保数据\\产品基本信息.txt",'a',encoding='utf-8')

    for i in range(1,nrows):
        print("------------------------------------------------------------------------------------------")
        link = table.cell(i, 0).value
        name = table.cell(i, 1).value
        page = table.cell(i, 2).value
        type = table.cell(i, 3).value
        product_dict = parse_product_page(page,link,name,type)
        product_dict_text.write(str(product_dict)+"\n")
        print(product_dict)