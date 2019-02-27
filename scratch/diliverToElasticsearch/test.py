#   @author: 马朝威 1570858572@qq.com
#   @time: 2019-02-21 22:44
import elasticsearch
import datetime
import json
import os


es_index = 'scratch'
es_type = "test-type"
es_client = elasticsearch.Elasticsearch()

def read_project(file_path):

    f = open(file=file_path, encoding='utf-8', mode='r')
    body = json.load(f)
    print(body)
    id = int(body['id'])
    es_client.index(index=es_index, doc_type="test-type", id=id, body=body)

def read_file():
    list_dir = 'E:\\scratch\\scratchproject'

    for file_name in os.listdir(list_dir):
        file_path = list_dir + '\\' + file_name
        print(file_path)
        read_project(file_path)
        break

def test():
    body = {"any": "data", 'a': {'b': 'c'}}
    print(type(body))
    id = 89
    es_client.index(index=es_index, doc_type="test-type", id=id, body=body)

def main():
    read_file()

if __name__ == "__main__":
    main()









