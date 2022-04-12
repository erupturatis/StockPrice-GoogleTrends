from webscrapping.google_trends import GoogleTrendsRequest
from webscrapping.stocks import StockTrendsRequester

class Main(object):

    def __init__(self) -> None:
        pass

    def correlation_flow(self)->None:

        trend_data = self.trend_object.save_trend_data(keyword=self.trend)
        stock_data = self.stock_object.save_stock_data(keyword=self.stock)

    

    def calculate_correlation(self, stock:str="tesla", trend:str="gas prices")->int:
        self.stock = stock
        self.trend = trend
        self.stock_object = StockTrendsRequester()
        self.trend_object = GoogleTrendsRequest()
        self.correlation_flow()


    def get_data(self)->None:
        pass


        


if __name__ == "__main__":
    main = Main()
    main.calculate_correlation(stock="apple",trend="ukraine")
