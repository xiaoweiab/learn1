import os
import json
from zone.province_city import province_and_city

zone_dict = {

    '东北' : ['黑龙江省','吉林省','辽宁省'],
    '华东' : ['上海市','江苏省','浙江省','安徽省','福建省','江西省','山东省','台湾省'],
    '华北' : ['北京市','天津市','山西省','河北省','内蒙古自治区'],
    '华中' : ['河南省','湖北省','湖南省'],
    '华南' : ['广东省','广西壮族自治区','海南省','香港特别行政区','澳门特别行政区'],
    '西南' : ['四川省','贵州省','云南省','重庆市','西藏自治区'],
    '西北' : ['陕西省','甘肃省','青海省','宁夏回族自治区','新疆维吾尔自治区']

}

def query_zone(province):

    for zone in zone_dict.keys():
        for pro in zone_dict[zone]:
            if province in pro:
                return zone



if __name__ == '__main__':

    zone_province_city_dict = {

        '东北': {},
        '华东': {},
        '华北': {},
        '华中': {},
        '华南': {},
        '西南': {},
        '西北': {}
    }

    for province in province_and_city.keys():

        zone = query_zone(province)
        zone_province_city_dict[zone].__setitem__(province,province_and_city[province])
    zone_province_city_json = json.dumps(zone_province_city_dict,indent=3,ensure_ascii=False)
    print(zone_province_city_json)
