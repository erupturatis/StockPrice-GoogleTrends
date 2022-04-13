
from datetime import datetime, timedelta
from webscrapping.google_trends import GoogleTrendsRequest
from webscrapping.stocks import StockTrendsRequester

import pandas as pd
import numpy as np

class Main(object):

    
    DAYS = 90
    def __init__(self) -> None:
        pass

    def write(text:str=' ',file_name:str='textfile'):
        file = open(f'{file_name}.txt','w')
        file.write(text)
        file.close()
    
    

    def correlation_flow(self)->list:

        trend_data = self.trend_object.get_trend_data(keyword=self.trend)
        stock_data = self.stock_object.get_stock_data(keyword=self.stock)

        today = datetime.today()
        n_days_ago = today - timedelta(days=self.DAYS)


        n_days_ago_string = str(n_days_ago) 
        n_days_ago_string = n_days_ago_string[:10]
        aux = n_days_ago_string.split("-")
        n_days_ago_string = f"{aux[1]}/{aux[2]}/{aux[0]}"

        trend_ind = 0
        stock_ind = 0

        stock_values = list()
        trend_values = list()
        # there is a slight date decalation between the starting date so
        # I am getting the common starting point for both
        for element in trend_data:
            if element['time'] == n_days_ago_string:
                break
            trend_ind += 1

        for element in stock_data:
            if element['time'] == n_days_ago_string:
                break
            stock_ind += 1

        minimum = min((len(trend_data)-trend_ind),(len(stock_data)-stock_ind))

        for i in range(minimum):
            #converts to standard format
            stock_values.append(float(stock_data[stock_ind]['value']))
            trend_values.append(trend_data[trend_ind]['value'])
            
            stock_ind += 1
            trend_ind += 1
        
        arr1 = np.array(stock_values)
        arr2 = np.array(trend_values)

        var = np.corrcoef(arr1,arr2)
        return var
      

              
    def calculate_correlation(self, stock:str="tesla", trend:str="gas prices")->list:
        self.stock = stock
        self.trend = trend
        self.stock_object = StockTrendsRequester()
        self.trend_object = GoogleTrendsRequest()
        return self.correlation_flow()


    def get_data(self)->None:
        pass


        


if __name__ == "__main__":
    main = Main()
    matrix = main.calculate_correlation(stock="microsoft",trend="ukraine")
    print(matrix)
