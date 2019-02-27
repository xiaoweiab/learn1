from lxml import etree
import xlrd
import requests
import os


tiaokuan_link_dict_list = list()

def parse_detail(page,link,name):
    product_dict = dict()
    product_dict.__setitem__('产品名称', name)
    product_dict.__setitem__('产品链接', link)
    tree = etree.HTML(page)

    ul = tree.xpath('//ul[@class="clearfix ul002"]/li/text()')
    product_dict.__setitem__('产品特色',ul)

    td = tree.xpath('//tr[@valign="top"]/td[2]/text()')[0].replace('\n','').replace('\t','')
    product_dict.__setitem__('产品简介', td)


    tiaokuan_lis = tree.xpath('/html/body/div/div[1]/ul/li')
    if len(tiaokuan_lis) == 0 :
        product_dict.__setitem__('产品条款', "none")
    else:
        tiaokuan_dict  = dict()
        for li in tiaokuan_lis:
            tiaokuan_name = li.xpath('./a/text()')[0]
            tiaokuan_link = li.xpath('./a/@href')[0]
            tiaokuan_dict.__setitem__("条款名称",tiaokuan_name)
            tiaokuan_dict.__setitem__("条款链接", tiaokuan_link)
        tiaokuan_link_dict_list.append(tiaokuan_dict)
        product_dict.__setitem__('产品条款',tiaokuan_dict)

    return product_dict

if __name__ == '__main__':

    data = xlrd.open_workbook('C:\\Users\\Hasee\\Desktop\\放心保数据\\catagory.xlsx')
    table = data.sheets()[0]
    nrows = table.nrows

    product_dict_text = open("C:\\Users\\Hasee\\Desktop\\放心保数据\\产品信息.text",'a',encoding='utf-8')

    for i in range(1,nrows):
        # print(i)
        link = table.cell(i, 0).value
        name = table.cell(i, 1).value
        page = table.cell(i, 2).value
        type = table.cell(i, 3).value
        product_dict = parse_detail(page,link,name)
    #     product_dict_text.write(str(product_dict)+"\n")
    #
    # print("ok")

    print(len(tiaokuan_link_dict_list))
    for tiaokuan_link_dict in tiaokuan_link_dict_list:
        tiaokuan_name = tiaokuan_link_dict["条款名称"]
        tioakuan_link = tiaokuan_link_dict["条款链接"]
        file_name = "C:\\Users\\Hasee\\Desktop\\放心保数据\\保险条款\\" + tiaokuan_name + ".pdf"
        if os.path.exists(file_name):
            print(tiaokuan_name+"已存在")
        else:
            response  = requests.get(tioakuan_link)
            response.raise_for_status()
            playFile = open(file_name, 'wb')
            for chunk in response.iter_content(100000):
                playFile.write(chunk)
            playFile.close()
            print(tiaokuan_name+"下载完成")





