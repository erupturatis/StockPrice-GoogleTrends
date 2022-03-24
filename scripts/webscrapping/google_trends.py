import json
from sqlite3 import paramstyle
from urllib import request
import requests 

class GoogleTrendsRequest(object):

    STANDARD_URL = "https://trends.google.com/trends/api/explore"
    HL = "en-US"
    TZ = -120
    def __init__(self,) -> None:
        pass

    def request_trends(self) -> object:

        return self


    def test_request(self):
        s = requests.Session()
        payload = dict()
        
        items = [
            {
               "keyword":"ukraine",
                "geo":"",
                "time":"today+3-m" 
            }
        ]
        req = {
            'comparisonItem':items,
            'category':0,
            'property':''
        }

        payload = {
            'hl':'en-US',
            'tz':-120,
            'req': req
        }
        element = open("textfile.txt","w")
        element.write(json.dumps(payload))
        element.close
        url = 'https://trends.google.com/trends/api/explore/pickers/geo'
        get_request = s.get(url = url, params= payload)
        print("ceva orice")
        #print(get_request.text)


        return
