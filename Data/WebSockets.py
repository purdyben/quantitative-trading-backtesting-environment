import websocket, json
import dateutil.parser

"""
pulling coinbase websocket information 
"""
minutes_processed = {}
minute_candlestick = []
current_tick = None
prevous_tick = None

def onOpen(ws):
    print("opening channel")
    subscribe_message= {
        "type":"subscribe",
        "channels":[{
            "name":"ticker",
            "product_ids":["BTC-USD"]
        }]
    } 
    ws.send(json.dumps(subscribe_message))

def onMessage(ws,message):
    print(json.loads(message))
    global current_tick, prevous_tick
    prevous_tick = current_tick
    current_tick = json.loads(message)
    print("Recevied Tick: ############")
    print("{} @ {}".format(current_tick['time'],current_tick['price']))
    DateTimeObject = dateutil.parser.parse(current_tick['time'])
    tick_dt =DateTimeObject.strftime("%m/%d/%Y %H:%M:%S")
    if not tick_dt in minutes_processed:
        minutes_processed[tick_dt] = True
        if len(minute_candlestick) > 0:
            minute_candlestick[-1]['close'] = prevous_tick['price'] 
        minute_candlestick.append({
            "minute" : tick_dt,
            "open": current_tick['price'],
            "high": current_tick['price'],
            "low": current_tick['price'],
        })
    if len(minute_candlestick) > 0:
        current_candlestick = minute_candlestick[-1]
        if current_candlestick['price'] > current_candlestick['high']:
            current_candlestick['high'] = current_candlestick['price']
        if current_candlestick['price'] < current_candlestick['low']:
            current_candlestick['low'] = current_candlestick['price']

socketURL  = "wss://ws-feed.pro.coinbase.com"

ws = websocket.WebSocketApp(socketURL, on_open=onOpen, on_message=onMessage)
print("Running")
ws.run_forever()