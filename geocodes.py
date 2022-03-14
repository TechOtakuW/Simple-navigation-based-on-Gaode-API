import requests #用于API HTTP requests
#使用python字典构造 parameters 请求函数
#API使用请求函数
key = 'xxxxxxxxxxxxxxxxxxxxxxxx' #高德地图API 获取key
def geo(address:str,city=None)-> dict:
    """获取地理编码
    address可填入国家、省份、城市、区县、城镇、乡村、街道、门牌号码等名称
    填入address对应city可查询具体经纬度
    """

    parameters = {
        'key': key,
        'city': city,
        'citylimit': True,
        'address': address
    }
    r = requests.get("https://restapi.amap.com/v3/geocode/geo?parameters",params=parameters)
    data = r.json()['geocodes'][0]['location']
    return data

