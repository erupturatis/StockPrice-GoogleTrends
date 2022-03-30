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

    def __init__(self) -> None:
        pass   


    def get_cookie(self):
        '''
        Gets a google cookie in order to not get error 429 too many requests
        '''
        cookie_req = self.session.get(url=self.GEO_URL)
        self.headers = cookie_req.request.headers

    def init_requester(self):
        session = requests.session()
        self.session = session

    def verification_needed(func):
        #decorator to call verify_initialization on all functions where is needed 
        def function_wrapper(*args):
            self = args[0]
            self.verify_initialization()
            func(self)
        return function_wrapper


    def get_request(self, url, **payload):
        # gets the actual payload
        payload = payload['payload']
        # makes the request and returns the object
        get_req = self.session.get(url=url, params = payload, headers = self.headers)
        return get_req


    def get_trend(self, days = 90) -> list:
        pass
    

    def get_tokens(self, keyword = 'ukraine') -> None:
        # get the tokes needed to create the request for trend over time
        payload = {
            'hl':'en-US',
            'tz':'-180',
            'req':{'comparisonItem':[{f'{keyword}':'ukraine','geo':'','time':'today 3-m'}],'category':0,'property':''},
        }
        payload['req'] = json.dumps(payload['req'])

        get_req = self.get_request(self.STANDARD_URL, payload = payload)
        print(get_req.text['widgets'])


    def verify_initialization(self):
        # if a session is not created yet, it will make one 
        if hasattr(self, 'session'):
            print("session already created")
        else:
            self.init_requester()
            print("creating session ")
            

    @verification_needed
    def get_trend_flow(self, keyword = 'ukraine', days = 90) -> None:
        if not hasattr(self, 'headers'):
            self.get_cookie()

        self.get_tokens(keyword=keyword)

        response = self.get_trend(days=days)
            
        

    

    def test_stuff(self):

        self.init_requester()
        self.get_cookie()

        payload = {
            'hl':'en-US',
            'tz':'-180',
            'req':{'comparisonItem':[{f'{keyword}':'ukraine','geo':'','time':'today 3-m'}],'category':0,'property':''},
        }
        payload['req'] = json.dumps(payload['req'])

        element = open("textfile.txt",'w')

        get_req = self.get_request(self.STANDARD_URL, payload = payload)
        print(get_req.text['widgets'])

        #print(get_request.request.headers)
        element.write(get_req.text) 
        element.close()


        return


    
   

trends_requester = GoogleTrendsRequest()
#trends_requester.test2 = trends_requester.decorator(trends_requester.test2)
trends_requester.test2()