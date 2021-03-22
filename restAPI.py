import requests
import json

print("start restAPI test")

url_items = "http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd"

params = {
#    "id": 4,
#    "content": "Python",
#    "completed": True
     "mktsel":"ETF",
     "bld":"dbms/comm/finder/finder_secuprodisu",
     "searchText":"KODEX CHINA"
    }

response = requests.post(url_items, data=params)

print(response.text)

json_object = json.loads(response.text)

json_string = json.dumps(json_object, indent=5, ensure_ascii=False)
print(json_string)

json_Array = json_object.get("block1")

for list in json_Array:
    print(list.get("codeName"))
