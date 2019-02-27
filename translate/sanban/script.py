import requests
import json
import os
base = 'http://open.memect.cn/api/x3b/event/'
header = {'api_key': 'b3d828e2-fa8e-11e7-be38-b8aeedae5c08'}


f = open('E:\\新三板\\xinsanban.json', 'r')
all_data = json.load(f)['data']

data = []
for da in all_data:
    file_path = 'E:\\新三板\\event\\%s.json' % (da)
    is_exist = os.path.exists(file_path)
    if is_exist:
        pass
    else:
        data.append(da.strip('\n'))

while len(data) > 0:
    code = data.pop(0)
    url = base + code
    try:
        r = requests.get(url, headers=header, timeout=2).json()
        print(r)
    except Exception as e:
        print('error:', code)
        data.append(code + '\n')
    else:
        event = str(r['data'])
        # print(event)
        file = open('E:\\新三板\\event\\%s.json' % (code),'w',encoding='utf-8')
        file.write(event)
        file.close()

