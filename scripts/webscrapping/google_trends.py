import json
from sqlite3 import paramstyle
from urllib import request
from webbrowser import get
import requests
import urllib3 

class GoogleTrendsRequest(object):
    '''
    Webscrapper for Google Trends 
    '''
    STANDARD_URL = "https://trends.google.com/trends/api/explore"
    GEO_URL = "https://trends.google.com/trends/api/explore/pickers/geo"
    HL = "en-US"
    TZ = -120

    def __init__(self, keyword) -> None:
        self.keyword = keyword

    def request_trends(self):

        return self


    def get_cookie(self):
        """
        Gets a google cookie in order to not get error 429 too many requests
        """
        cookie_req = self.server.get(url=self.GEO_URL)

    def init_request(self):
        server = requests.session()
        self.server = server

    def get_request(self, url, **params):
        pass

    def get_trends(self):
        pass



    def test_request(self):
        self.get_cookie()
        payload = {
            'hl':'en-US',
            'tz':'-180',
            'req':{'comparisonItem':[{'keyword':'ukraine','geo':'','time':'today 12-m'}],'category':0,'property':''},
        }

        element = open("textfile.txt","w",encoding="utf-8")

        payload['req'] = json.dumps(payload['req'])
        url = 'https://trends.google.com/trends/api/explore'

        try:
            get_request = self.server.get(url, params = payload )
        except:
            print("request is not initialized")


        #print(get_request.request.headers)
        element.write(get_request.text) 
        element.close()


        return


trends_requester = GoogleTrendsRequest()
trends_requester.init_request()
trends_requester.test_request()