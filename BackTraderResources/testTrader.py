import backtrader as bt
import backtrader.feeds as btfeeds
import pandas as pd
import datetime
class trader():   
    """
    docstring
    """
    def printBal(self,note=""):
        print(note + ' Portfolio Value: %.2f' % self.cerebro.broker.getvalue())
    def getCash(self):
        return self.cerebro.broker.get_cash()
    def getBacktrader(self):
        return self.cerebro
    def setCash(self,num):
        self.cerebro.broker.set_cash(num)
    def addData(self,data):
        self.cerebro.adddata(data)
    def plotBt(self):
         self.cerebro.plot()
    def runCerebro(self):
        self.cerebro.run()
    def addStrat(self,Strategy):
        self.cerebro.addstrategy(Strategy)
    def addBinenceData(self,crypt_df):
        bt_data = bt.feeds.PandasDirectData(dataname=crypt_df, 
                # datetime=crypt_df.columns.get_loc('timestamp')+1, 
                fromdate=datetime.datetime(2017, 1, 1),
                # dtformat=('%Y-%m-%d'),
                datetime=crypt_df.columns.get_loc('date')+1,
                open=crypt_df.columns.get_loc('open')+1, 
                high=crypt_df.columns.get_loc('high')+1, 
                low=crypt_df.columns.get_loc('low')+1, 
                close=crypt_df.columns.get_loc('close')+1,
                volume=crypt_df.columns.get_loc('volume')+1,
                openinterest=-1,
                # reverse=False,
                timeframe=bt.TimeFrame.Days)

        self.cerebro.adddata(bt_data)
    def addGenericCSV(self,data,cerebro):
        CVS_data = bt.feeds.GenericCSV(
            # fromdate=datetime.datetime(2017, 1, 1),
            # todate=datetime.datetime(2020, 9, 1),
            dataname='2020_BTCUSDT_1_Day.csv',
            fromdate=datetime.datetime(2017, 1, 1),
            dtformat=('%Y-%m-%d '),
            tmformat=('%H:%M:%S'),
            datetime=0,
            high=2,
            low=3,
            open=1,
            close=4,
            volume=5,
            openinterest=-1,
            timeframe=bt.TimeFrame.Days,
        )
        cerebro.adddata(CVS_data)
    def __init__(self):
        self.cerebro = bt.Cerebro()
        CVS_data = bt.feeds.GenericCSVData(
                        dataname='2020_BTCUSDT_1_Day.csv',
                        # dtformat ( %Y-%m-%d %H:%M:%S),
                        # Do not pass values before this date
                        fromdate=datetime.datetime(2017, 1, 1),
                        # Do not pass values after this date
                        # todate=datetime.datetime(2020, 8, 21),
                         timeframe=bt.TimeFrame.Days,
                        datetime=0,
                        high=2,
                        low=3,
                        open=1,
                        close=4,
                        volume=5,
                        openinterest=-1)
                    
        self.cerebro.adddata(CVS_data)
        
       
       