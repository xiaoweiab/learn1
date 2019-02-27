import requests
import os
import json
import re

def colect_tag(json_lines):
    for json_line in json_lines:

        try:
            json_line_content = json.loads(json_line)
            for json_tag in json_line_content.keys():
                set1.add(json_tag)
        except:
            print(json_line)



def add_collection(json_lines):
    result_file = open('result.csv', 'a', encoding='utf-8')
    title_string = 'album;language;code;scene;genre;lyrics;mood;tag;' \
                   'scence;artist;song'
    result_file.write(title_string+'\n')
    for json_line in json_lines:

        try:
            set1 = ['album', 'language', 'code', 'scene', 'genre', 'lyrics',
                    'mood', 'tag', 'scence', 'artist','song' ]
            song_dict = dict()
            for element in set1:
                song_dict.__setitem__(element, "")

            json_line_content = json.loads(json_line)
            for json_tag in json_line_content.keys():
                tag_content  = json_line_content[json_tag]
                json_tag1 = json_tag.strip()
                song_dict[json_tag1] = tag_content
            result_String = ';'.join(song_dict.values())
            result_file.write(result_String+'\n')
        except:
            # print("json_line)
            pass




if __name__ == '__main__':

    file_path = "C:\\Users\\Hasee\\Desktop\\task2_data_traindev\\task2_data_train&dev\\训练集.txt"
    file = open(file_path,'r',encoding='utf-8')
    data = file.read()
    json_lines  = re.findall('(\{.*?})',data)
    add_collection(json_lines)

