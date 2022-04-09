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
       
    def get_stock(self, symbol) -> list:
        '''
        makes use of another powershell file to fetch the data because 
        python requests library doesn t work for some reason
        '''
        powershell = f"powershell scripts/webscrapping/request_stock.ps1 TSLA 2021-10-09 2022-04-09"
        response = subprocess.check_output(powershell, shell=True)
        # decodes and turn response into pytohn dictionary
        response = response.decode("utf-8")
        response = json.loads(response)
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

        print(self.days_ago)
        print(self.yesterday)



    def get_stock_data(self, keyword:str='TSLA', days:int=90 ) -> list:
        self.get_stock_flow(keyword,days)


    @verification_needed
    def get_stock_flow(self, keyword:str='TSLA', days:int = 90) -> None:
        #default flow for all requests
        symbol = self.get_search_result(keyword=keyword)
        result = self.get_stock(symbol)
        print(result)


if __name__ == '__main__':

    st = StockTrendsRequester()
    st.get_stock_data('apple',120)
   
    

 