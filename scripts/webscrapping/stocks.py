
from sqlite3 import paramstyle
import requests
import pandas as pd

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
        payload = {
            'search': keyword
        }

        headers = {
            'origin':'https://www.nasdaq.com'
        }
     

        req = self.session.get(self.SEARCH_URL,params=payload, headers=headers, timeout=5)
        print(req.text)

    
    def get_stock_data(self, keyword:str='TSLA', days:int=90 ) -> list:
        self.get_stock_flow(keyword,days)


    @verification_needed
    def get_stock_flow(self, keyword:str='TSLA', days:int = 90) -> None:
        self.get_search_result(keyword=keyword)
        #req = self.session.get(self.URL_PART1 + keyword + self.URL_PART2)


if __name__ == '__main__':
    st = StockTrendsRequester()
    st.get_stock_data('apple',90)