import elasticsearch
import datetime
import json
import os

#   @author: 马朝威 1570858572@qq.com
#   @time: 2019-02-21 19:51

es_index = 'scratch'
es_type = 'all'
es_client = elasticsearch.Elasticsearch(['localhost:9200', ])

def read_project(file_path):

    f = open(file=file_path, encoding='utf-8', mode='r')
    body = json.load(f)
    id = int(body['id'])
    es_client.create(index=es_index, doc_type=es_type, id=1, body= body)



def main():
    list_dir = 'E:\\scratch\\scratchproject'
    # print(es_client.info)
    # print(es_client.explain)
    for file_name in os.listdir(list_dir):
        file_path = list_dir +'\\'+file_name
        print(file_path)
        read_project(file_path)
        break


if __name__ == "__main__":
    main()









