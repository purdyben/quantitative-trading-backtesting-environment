
import config, csv
from binance.client import Client
import binanceConfig as config
import time
from datetime import datetime
def convertBinanceDates(dataf):
    l = []
    print(len(dataf))
    for date in dataf:          
        l.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(date))))
    print(len(l))
    return l
def convertBinanceDate(date):   
    return str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(date))))

def convertBinanceDateTMD(date):  
    return str(time.strftime("%Y-%m-%d", time.localtime(int(date))))

client = Client(config.API_KEY, config.API_SECRET)
def getBinanceCsvData(symbol,interval,fileName):
    csvfile = open(fileName, 'w', newline='') 
    candlestick_writer = csv.writer(csvfile, delimiter=',')

    # # candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Jan, 2020", "12 Jul, 2020")
    # candlesticks = client.get_historical_klines(symbol, interval, "1 Jan, 2017", "12 Jul, 2020")
    # klines = client.get_historical_klines("ETHBTC", Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2017", "1 Jan, 2018")
    candlesticks = client.get_historical_klines(symbol, interval, "1 Jan, 2017", "1 Sep, 2020")
    # for price in client.get_all_tickers():
    #     print(price)
    candlestick_writer.writerow(['Date','Open','High','Low','Close','Volume'])
    for candlestick in  candlesticks:
        candlestick[0] = convertBinanceDate(candlestick[0] / 1000)
        candlestick_writer.writerow(candlestick[:6])
    print("closing")
    csvfile.close()

print("getting 2020_BTCUSDT_1_weeks.csv")
getBinanceCsvData('BTCUSDT',Client.KLINE_INTERVAL_1WEEK,'2020_BTCUSDT_1_weeks.csv')   
# print("getting 2020_BTCUSDT_1_Day.csv")
# getBinanceCsvData('BTCUSDT',Client.KLINE_INTERVAL_1DAY,'2020_BTCUSDT_1_Day.csv')
# print("getting 2020_BTCUSDT_4_hour.csv")
# getBinanceCsvData('BTCUSDT',Client.KLINE_INTERVAL_4HOUR,'2020_BTCUSDT_4_hour.csv')
# print("getting 2020_BTCUSDT_2_hour.csv")
# getBinanceCsvData('BTCUSDT',Client.KLINE_INTERVAL_2HOUR,'2020_BTCUSDT_2_hour.csv')
# print("getting 2020_BTCUSDT_1_hour.csv")
# getBinanceCsvData('BTCUSDT',Client.KLINE_INTERVAL_1HOUR,'2020_BTCUSDT_1_hour.csv')
# print("getting 2020_ETHBTC_1_Day.csv")
# getBinanceCsvData('ETHBTC',Client.KLINE_INTERVAL_1DAY,'2020_ETHBTC_1_Day.csv')
# print("getting 2020_ETHBTC_4_hour.csv")
# getBinanceCsvData('ETHBTC',Client.KLINE_INTERVAL_4HOUR,'2020_ETHBTC_4_hour.csv')
# getBinanceCsvData('BTCUSDT',Client.KLINE_INTERVAL_15MINUTE,'2020_BTCUSDT_15_minutes.csv')
# getBinanceCsvData('BTCUSDT',Client.KLINE_INTERVAL_1MINUTE,'2020_BTCUSDT_1minutes.csv')

