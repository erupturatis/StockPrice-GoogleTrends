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
      
        payload = {
            'hl':'en-US',
            'tz':'-120',
            'req':{"comparisonItem":[{"keyword":"urkaine","geo":"","time":"now 7-d"}],"category":0,"property":""} ,

        }
        payload["req"] = json.dumps(payload["req"])
        element = open("textfile.txt","w",encoding="utf-8")
        

        url = 'https://trends.google.com/trends/api/explore'
        url2 = 'https://trends.google.com/trends/api/explore'
        get_request = s.get(url = url2, params= payload)
        print(get_request.text)
        element.write("new")
        element.write(get_request.text)
        element.close()


        return


trends_requester = GoogleTrendsRequest()
trends_requester.test_request()