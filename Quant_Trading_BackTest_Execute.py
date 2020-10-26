import pandas as pd
import Data.DataStream as DS
import PlotingResources.GraphPlot as plot
import BackTraderResources.testTrader as btrader
import binance as Binance
import backtrader as bt
from backtrader_plotting import Bokeh
from backtrader_plotting.schemes import Tradimo

# from strats import *
from MyStrategys.placeHolder import *
from MyStrategys.FirstStratagy import *

def Main():
    """
    Gets selected data
    """
    # dataStream = DS.dataStream()
    print("#### Data Processing  ####")
    # btheaders = ['timestamp','open','high','low','close','volume','Close time','Quote asset volume','Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume']
    # df = pd.read_csv("2020_BTCUSDT_1_Day.csv",names= btheaders)
    # final_df = df[['open','high','low','close','volume']]
    # final_df.reset_index(drop=True, inplace=True)
    # final_df['date'] = (convertBinanceDates(df.index))
    
    # df = pd.read_csv("GSPC.csv")
    # print(df.head)
    """it
    create trader 
    """
    print("#### Creating Trader ####")
    trader = btrader.trader()
    startBal = trader.getCash()
    # """
    # run trader
    # """
    trader.addStrat(TestStarat)
    trader.runCerebro()
    print("Starting cash " + str(startBal))
    trader.printBal('Ending')
    """
    Prints data 
    """
    print("#### Print Results ####")
    b = Bokeh(style='bar', plot_mode='single')
    
    # plotconfig = {
    #     'id:ind#0': dict(
    #         subplot=True,
    #     ),
    # }
    # b = Bokeh(style='bar', plot_mode='single', scheme=Blackly Scheme, plotconfig=plotconfig)
    trader.plotBt(b)
    
   



if __name__ == '__main__':
	Main()