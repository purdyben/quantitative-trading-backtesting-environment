import pandas as pd
import Data.DataStream as DS
import PlotingResources.GraphPlot as plot
import BackTraderResources.testTrader as btrader
import binance as Binance
import backtrader as bt
import datetime
from strats import TestStrategy

def Main():
    """
    Gets selected data
    """
    # dataStream = DS.dataStream()
    # df = dataStream.historicalData
    # df = df.rename({'index': 'time'}, axis=1)
    print("#### Data Processing  ####")
    # btheaders = ['timestamp','open','high','low','close','volume','Close time','Quote asset volume','Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume']
    # df = pd.read_csv("2020_BTCUSDT_1_Day.csv",names= btheaders)
    # final_df = df[['timestamp','open','high','low','open','close','volume']]

    """
    create trader 
    """
    print("#### Creating Trader ####")
    

    trader = btrader.trader()
    # trader.addBinenceData(final_df)
    
    """
    run trader
    """
    trader.addStrat(TestStrategy)
    trader.runCerebro()
    
    trader.printBal()
    trader.plotBt();
    """
    Prints data 
    """
    print("#### Print Results ####")
    # trader.plotBt();
    # plot.PlotData(df,"yf", buy_signals=False,sell_signals=False)



if __name__ == '__main__':
	Main()