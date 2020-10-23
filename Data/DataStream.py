from pandas_datareader import data as pdr
from datetime import date
import datetime as dt
import pandas as pd
import yfinance as yf
yf.pdr_override()



import json
import requests
import binance as Binance


class dataStream():
    def getYfData(self,today,start_date):#start_date,today,ticker
        """
        return pandas dataframe of yahoo finace data.
        """

        #self.ticker_list=[‘DJIA’, ‘DOW’, ‘LB’, ‘EXPE’, ‘PXD’, ‘MCHP’, ‘CRM’, ‘JEC’ , ‘NRG’, ‘HFC’, ‘NOW’]
        print("Getting Data from yfinance from " + (str) (today) + " to " + (str)(start_date))
        # return yf.download(self.ticker_list, start="2017-01-01", end="2017-04-30")
        print(today)
        print((str)(today))
        return yf.download(self.ticker_list, start="2017-01-01", end=(str)(today))
    
    def get_bars(self,symbol, interval = '1h'):
        root_url = 'https://api.binance.com/api/v1/klines'
        url = root_url + '?symbol=' + symbol + '&interval=' + interval
        data = json.loads(requests.get(url).text)
        df = pd.DataFrame(data)
        df.columns = ['open_time',
                        'Open', 'High', 'Low', 'Close', 'Volume',
                        'close_time', 'qav', 'num_trades',
                        'taker_base_vol', 'taker_quote_vol', 'ignore']
        df.index = [dt.datetime.fromtimestamp(x/1000.0) for x in df.close_time]
        return df
    def getBinanceData(self,symbol, interval = '5m'):
        return self.get_bars(symbol,interval)
        # symbol = 'STEEMETH'
        # interval = '1h'





    
    """ 
    Gets and holds historical data for backtesting
    """
    def __init__(self):
        self.ticker_list=["^GSPC"]
        # #self.ticker_list=[‘DJIA’, ‘DOW’, ‘LB’, ‘EXPE’, ‘PXD’, ‘MCHP’, ‘CRM’, ‘JEC’ , ‘NRG’, ‘HFC’, ‘NOW’]
        self.today = "2018-4-12"
        self.start_date = "2010-01-01"
        # print("Getting Data from yfinance from " + (str) (self.today) + " to " + (str)(self.start_date))
        self.historicalData = self.getYfData(self.today,self.start_date)
        # PlotData(df, trends=lines, plot_title=symbol+" trends")
    
    