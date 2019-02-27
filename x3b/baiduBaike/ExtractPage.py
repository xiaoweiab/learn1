import os
# from lxml import etree
from bs4 import BeautifulSoup

# def extract_name(tree):
#     title = tree.xpath(
#         './/dd[@class="lemmaWgt-lemmaTitle-title"]/h1/text()')
#     return title

def extract_name(soup):
    try:
        content = soup.find('dd',class_="lemmaWgt-lemmaTitle-title")
        name = content.find('h1').get_text()
        return name
    except:
        return None

def extract_content(soup):
    try:
        content = soup.find('div', class_="main-content")
        content1 = content.find('div', class_="main_tab main_tab-defaultTab curTab")
        content2 = content1.find('div', class_='para-title level-2')
        # print(type(content2))
        result_content = ""
        for sibling in content2.next_siblings:

            if isinstance(sibling, type(content2)):
                # print(sibling.attrs)
                if sibling.attrs['class'][0] == 'anchor-list':
                    break
                else:
                    result_content = result_content + sibling.get_text().replace(' ', '').replace('\n', '')
            else:
                pass
        result_content.replace(' ', '').replace('\n', '')
        return result_content
    except:
        return None




if __name__ == '__main__':
    path = 'E:\\知识图谱实验室\\数据集\\百度百科电影1\\'
    path1 = 'E:\\知识图谱实验室\\数据集\\百度电影简介\\'
    file_list = os.listdir(path)
    for i, file_name in enumerate(file_list):
        print(i)
        file_path = path + file_name
        file = open(file_path, 'r', encoding='utf-8')
        content = file.read()
        soup = BeautifulSoup(content,"lxml")
        name = extract_name(soup)
        if name  :
            result = extract_content(soup)
            name = name.replace('/','')
            if result:
                file_path_1 = path1+name+'.txt'
                if os.path.exists(file_path_1) :
                    print(name + ": exists")
                else:
                    file_2 = open(file_path_1, 'w', encoding='utf-8')
                    file_2.write(result)


                # print(result)
        else:
            print(str(i)+"  "+file_name)
        # break

