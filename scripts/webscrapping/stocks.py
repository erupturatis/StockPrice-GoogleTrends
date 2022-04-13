import json

import re
import subprocess

import requests
import pandas as pd
from datetime import datetime, timedelta

class StockTrendsRequester(object):

    STOCK_URL_PART1 = 'https://api.nasdaq.com/api/quote/'
    STOCK_URL_PART2 = '/chart'
    SEARCH_URL = 'https://api.nasdaq.com/api/autocomplete/slookup/10'

    def __init__(self) -> None:
        pass

    def verify_initialization(self):
        # if a session is not created yet, it will make one 
        if hasattr(self, 'session'):
            print("session already created")
        else:
            self.init_requester()
            print("creating session ")

    def init_requester(self) -> None:
        session = requests.session()
        self.session = session

    
    def verification_needed(func):
        #decorator to call verify_initialization on all functions where is needed 
        def function_wrapper(*args):
            
            self = args[0]
            self.verify_initialization()
            func(*args)
        return function_wrapper


    def get_search_result(self,keyword:str) -> str:
        '''
        Uses the company name to get the first search result on the website 
        This allows you to simply call the function with the company name instead
        of the stock abbreviation
        It uses the data for the stock fetching
        '''
        
        powershell = f"powershell scripts/webscrapping/request.ps1 {keyword}"
        response = subprocess.check_output(powershell, shell=True)
        response = response.decode("utf-8")
        return json.loads(response)["data"][0]["symbol"]

       
    def get_stock(self, symbol, days:int) -> list:
        '''
        makes use of another powershell file to fetch the data because 
        python requests library doesn t work for some reason
        '''
        
        self.get_day(days=days)
        powershell = f"powershell scripts/webscrapping/request_stock.ps1 {symbol} {self.days_ago} {self.yesterday}"
        response = subprocess.check_output(powershell, shell=True)
        # decodes and turn response into pytohn dictionary
        response = response.decode("utf-8")
        response = json.loads(response)

     
        if response['status']['rCode'] == 400:
            raise ValueError(str(response['status']['bCodeMessage'][0]['errorMessage']) )
        
        
        return response["data"]["chart"]


    def write(self,text=' ',file:str='textfile') -> None:
        text_file = open(f'{file}.txt','w')
        text_file.write(text)
        text_file.close()


    def get_day(self, days:int)->None:
        today = datetime.today()
        self.days_ago = str(today - timedelta(days=days))
        self.yesterday = str(today - timedelta(days=1))
        self.days_ago = self.days_ago[:10]
        self.yesterday = self.yesterday[:10]



    def get_stock_data(self, keyword:str='TSLA', days:int=90 ) -> list:
        self.get_stock_flow(keyword,days)
        return self.data


    def save_stock_data(self, keyword:str='TSLA', days:int=90 ) -> list:
        self.get_stock_flow(keyword,days)
        self.dataframe.to_csv(f'{keyword}.csv')
    

    def fill_blank_days(self,result:list,days:int)->list:
        # Normalizing the data, filling the missing day spaces
   
        final_result = result
        today = datetime.today()
        days_count = days
        
        for i in range(0,days-1):
            days_ago1 = str(today - timedelta(days=days_count-i))
            days_ago1 = days_ago1[:10]
            d1 = days_ago1.split("-")
            days_ago1 = f"{d1[1]}/{d1[2]}/{d1[0]}"
            #brings the dates to the same format as result date

            
            if not final_result[i]['time']==days_ago1:
                final_result.insert(i,{
                    'value': result[i]['value'],
                    'time': days_ago1
                })

        
        return final_result



    @verification_needed
    def get_stock_flow(self, keyword:str='TSLA', days:int = 90) -> None:
        #default flow for all requests

        symbol = self.get_search_result(keyword=keyword)
        result = self.get_stock(symbol,days=days+1)

        values = list()
        times = list()
        data = list()
        
        simple_result = list()

        for element in result:
            simple_result.append({
                'value': element["z"]["value"],
                'time': element["z"]["dateTime"]
            })

        simple_result = self.fill_blank_days(simple_result,days=days+1)
  
        for element in simple_result:
            values.append(element["value"])
            times.append(element["time"])
            

        
        df = pd.DataFrame(
            {
            'values': values,
            'times': times
            } 
        )
        self.dataframe=df
        self.data = simple_result



if __name__ == '__main__':
    #for testing 
    st = StockTrendsRequester()
    st.save_stock_data('russian ruble',90)
   