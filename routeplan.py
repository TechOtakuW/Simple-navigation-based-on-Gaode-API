#route plan
import json
import requests
from geocodes import geo
key = '1fe97c7203cd1a04110ec439d230083e'



from_place = input("请输入起始地址")
from_location = geo(from_place)
to_place = input("请输入目的地")
to_place = geo(to_place)
type = input("出行方式(1.公交、2.步行、3.驾车、4.骑行)，请输入数字")



url="https://restapi.amap.com"
if type=="1":
    url = url+ "/v3/direction/transit/integrated?parameters"
elif type=="2":
    url = url + "/v3/direction/walking"
elif type=="3":
    url = url + "/v3/direction/driving"
elif type == "4":
    url = url + "/v4/direction/bicycling"



parameters = {
    'key': key,
    'origin': str(from_location),
    'destination': str(to_place),
    'extensions':'all',
    'strategy':'0',
    'output':'json',
    'city':'150100',
}



if type=="1":
   r = requests.get(url)
   data = r,json()['segments'][0]['bus']['buslines'][0]['name']
   print(data)
elif type=="2":
    r = requests.get(url)
    data = r,json()['instruction']
    print(data)
elif type=="3":
    r = requests.get(url)
    data = r,json()['instruction']
    print(data)
elif type=="4":
    r = requests.get(url)
    data = r,json()['insrtuction']
    print(data)


   
