import requests


# 得到经纬度信息
def get_position(name):
    url = f'http://api.map.baidu.com/geocoding/v3/?address={name}&output=json&ak={"QWvIBj7ebRmywj1dxzKgZwFqcLESKGQA"}'
    res = requests.get(url)
    val = res.json()
    lng = val['result']['location']['lng']
    lat = val['result']['location']['lat']
    return (lng, lat)


