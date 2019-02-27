import requests
import re

def get_page(link,name):
    page = requests.get(link).text
    print(page)



if __name__ == '__main__':

    file = open("G:\\沃保网\\财产保险链接.csv",'r')
    frist_line = True
    for line in file:
        if frist_line:
            frist_line = False
        else:
            line = line.replace("\n",'')
            list = line.split(';')
            link = list[0].replace("\"",'')
            name = list[1].replace("\"",'').replace(',','')
            get_page(link,name)
            break