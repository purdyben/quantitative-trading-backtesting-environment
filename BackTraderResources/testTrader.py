import backtrader as bt
import backtrader.feeds as btfeeds
import pandas as pd
import datetime
class trader():   
    """
    docstring
    """
    def printBal(self):
        print('Final Portfolio Value: %.2f' % self.cerebro.broker.getvalue())
    def getBacktrader(self):
        return self.cerebro
    def setCash(self,num):
        self.cerebro.broker.set_cash(num)
    def addPandasData(self,df):
        data = bt.feeds.PandasData(dataname=df)
        self.cerebro.adddata(data)
    def plotBt(self):
         self.cerebro.plot()
    def runCerebro(self):
        self.cerebro.run()
    def addStrat(self,Strategy):
        self.cerebro.addstrategy(Strategy)
    def addBinenceData(self,crypt_df):
        print(crypt_df.columns)
        bt_data = bt.feeds.PandasDirectData(dataname=crypt_df, 
                # datetime=crypt_df.columns.get_loc('timestamp')+1, 
                fromdate=datetime.datetime(2017, 1, 1),
                open=crypt_df.columns.get_loc('open')+1, 
                high=crypt_df.columns.get_loc('high')+1, 
                low=crypt_df.columns.get_loc('low')+1, 
                close=crypt_df.columns.get_loc('close')+1,
                volume=crypt_df.columns.get_loc('volume')+1,
                openinterest=-1,
                reverse=False,
                timeframe=bt.TimeFrame.Days)

        self.cerebro.adddata(bt_data)
    def __init__(self):
        self.cerebro = bt.Cerebro()
        final_df = bt.feeds.YahooFinanceCSVData(
                        dataname='GSPC.csv',
                        dtformat=('%Y-%m-%d'),
                        # Do not pass values before this date
                        fromdate=datetime.datetime(2019, 8, 21),
                        # Do not pass values after this date
                        todate=datetime.datetime(2020, 8, 21),
                        reverse=False)
        self.cerebro.adddata(final_df)
        
        print('Starting Portfolio Value: %.2f' % self.cerebro.broker.getvalue())
        
       
       