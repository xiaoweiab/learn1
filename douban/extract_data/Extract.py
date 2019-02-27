from lxml import etree
import os
import logging

def extract_name(tree):
    moive_name = tree.xpath('//*[@id="content"]/h1/span[1]/text()')[0]
    return moive_name

def extract_recommendation(tree):

    recomend_movies = tree.xpath('//*[@id="recommendations"]/div/dl')
    movie_dict_list = list()

    for movie in recomend_movies:
        movie_dict = dict()
        movie_dict['电影链接'] = movie.xpath('./dd/a/@href')[0].split('?')[0]
        movie_dict['电影名称'] = movie.xpath('./dd/a/text()')[0]
        movie_dict_list.append(movie_dict)

    return movie_dict_list

def extract_score(tree):

    rate_dict = dict()

    douban_score = tree.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')[0]
    rate_num = tree.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/div/div[2]/a/span/text()')[0]
    rate_dict['豆瓣评分'] = douban_score
    rate_dict['投票人数'] = rate_num

    ratings_on_weight = tree.xpath('//*[@id="interest_sectl"]/div[1]/div[3]')[0]
    rate_list = ratings_on_weight.xpath('.//span[@class="rating_per"]/text()')
    rate_dict['5星比例'] = rate_list[0]
    rate_dict['4星比例'] = rate_list[1]
    rate_dict['3星比例'] = rate_list[2]
    rate_dict['2星比例'] = rate_list[3]
    rate_dict['1星比例'] = rate_list[4]

    rating_betterthan = tree.xpath('//*[@id="interest_sectl"]/div[2]/a/text()')
    rate_dict['好于'] = rating_betterthan

    return rate_dict
def error_log(error_info):
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    handler = logging.FileHandler("log.txt")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.debug(error_info)

if __name__ == '__main__':

    file_set__path = "E:\\知识图谱实验室\\数据集\\豆瓣电影\\电影"
    output_file_path = "E:\\知识图谱实验室\\数据集\\豆瓣电影\\"+'豆瓣.txt'
    output_file = open(output_file_path,'a',encoding='utf-8')
    file_list = os.listdir(file_set__path)
    for i, file_name in enumerate(file_list):
        print(i)
        file_path = file_set__path+"\\"+file_name
        if i == 9959:
            print("抽取完成")
        else:
            try:
                file_content  = open(file_path,'r',encoding='utf-8').read()
                tree = etree.HTML(file_content)
                file_dict = dict()
                file_dict['电影名称'] = extract_name(tree)
                file_dict['推荐电影'] = extract_recommendation(tree)
                file_dict['电影评分']  = extract_score(tree)
                dict_string = str(file_dict)+"\n"
                output_file.write(dict_string)
            except:
                error_info = file_name+" "+str(i)+" error"
                error_log(error_info)
                print(error_info)

