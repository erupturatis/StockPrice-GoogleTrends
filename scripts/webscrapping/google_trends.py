
import json
from sre_constants import RANGE
from time import time
from urllib import request
from webbrowser import get
import requests
import urllib3 
import pandas as pd

class GoogleTrendsRequest(object):
    '''
    Webscrapper for Google Trends 
    '''
    MONTHS = {
        'Jan':'01',
        'Feb':'02',
        'Mar':'03',
        'Apr':'04',
        'May':'05',
        'Jun':'06',
        'Jul':'07',
        'Aug':'08',
        'Sep':'09',
        'Oct':'10',
        'Nov':'11',
        'Dec':'12'
    }

    STANDARD_URL = "https://trends.google.com/trends/api/explore"
    GEO_URL = "https://trends.google.com/trends/api/explore/pickers/geo"
    TREND_URL = "https://trends.google.com/trends/api/widgetdata/multiline"

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
            func(*args)
        return function_wrapper



    def get_request(self, url, **payload):
        # gets the actual payload
        payload = payload['payload']
        # makes the request and returns the object
        get_req = self.session.get(url=url, params = payload, headers = self.headers)
        return get_req


    def get_trend(self, keyword:str = '' ) -> list:
        #builds the payload
        payload = {
            'hl':'en-US',
            'tz':'-180',
            'req':{"time":f'{self.time}',"resolution":"DAY","locale":"en-US","comparisonItem":[{"geo":{},"complexKeywordsRestriction":{"keyword":[{"type":"BROAD","value":f"{keyword}"}]}}],"requestOptions":{"property":"","backend":"IZG","category":0}},
            'token':f'{self.token}'
        }
      
       
        payload['req'] = json.dumps(payload['req'])
        response = self.get_request(self.TREND_URL, payload=payload)
        #cuts the bad characters
        self.write(response.url)
        if response.status_code == 401:
            
            raise ValueError(" --------------- 401 bad response")
        else:
            print(response.status_code)
        needed_json = response.text[5:]
        #turns json to python dict
        needed_json = json.loads(needed_json)
        
        return needed_json['default']['timelineData']

    
    def write(self,text=' ',file:str='textfile') -> None:
        text_file = open(f'{file}.txt','w')
        text_file.write(text)
        text_file.close()


    def get_tokens(self, keyword:str = 'ukraine') -> None:
        # get the tokes needed to create the request for trend over time
        payload = {
            'hl':'en-US',
            'tz':'-180',
            'req':{'comparisonItem':[{'keyword':f'{keyword}','geo':'','time':'today 3-m'}],'category':0,'property':''},
        }
        payload['req'] = json.dumps(payload['req'])
        get_req = self.get_request(self.STANDARD_URL, payload = payload)
        # cuts the first part of the response ")]}'"
        response = get_req.text[5:]
        # stores the token and the time
        self.token = json.loads(response)['widgets'][0]['token']
        self.time = json.loads(response)['widgets'][0]['request']['time']
        


    def verify_initialization(self):
        # if a session is not created yet, it will make one 
        if hasattr(self, 'session'):
            print("session already created")
        else:
            self.init_requester()
            print("creating session ")
            

    @verification_needed
    def get_trend_flow(self, keyword:str = 'ukraine', days = 90) -> list:

        if not hasattr(self, 'headers'):
            self.get_cookie()

        self.get_tokens(keyword=keyword)
        response = self.get_trend(keyword=keyword)
        
        data = list()
        values = list()
        times = list()
        #gets only the wanted parameters

        times_new_format = list()

        for element in response:
            
            values.append(*element['value'])
            times.append(element['formattedTime'])

        for element in times:
            split_elements = element.split(' ')
            split_elements[1] = split_elements[1][:-1]
            if len(split_elements[1])==1:
                split_elements[1] = '0' + split_elements[1]
            new_element = self.MONTHS[split_elements[0]] + '/' + split_elements[1] + '/' + split_elements[2]
            times_new_format.append(new_element)
        
        for i in range(len(response)):
            packed = response[i]['value']
            unpacked = packed[0]
            data.append({
                'value': unpacked,
                'time':times_new_format[i]
            })
            
        
        

        df = pd.DataFrame(
            {
                'values': values,
                'times': times_new_format
            }
        )
        self.dataframe = df
        self.times = times_new_format
        self.values = values
        self.data = data

    

    def get_trend_data(self, keyword:str = 'ukraine') -> list:
        self.get_trend_flow(keyword)
        return self.data


    def get_trend_csv(self, keyword:str = 'ukraine') :
        self.get_trend_flow(keyword)
        return self.df


    def get_trend_values(self, keyword:str = 'ukraine') :
        self.get_trend_flow(keyword)
        return self.values


    def save_trend_data(self, keyword:str = 'ukraine') -> None:
        self.get_trend_flow(keyword)
        
        self.dataframe.to_csv(keyword+'.csv')


    
if __name__ == '__main__':
    #for testing 
    trends_requester = GoogleTrendsRequest()
    trends_requester.save_trend_data(keyword="ukraine")
    


