from breeze_connect import BreezeConnect
from pprint import pprint

# First step is to generate session

bz = BreezeConnect(api_key='8o2B51yPL4299698355J547H)82715&6')
bz.generate_session(api_secret='K30O0709@653S4*6505`D53277770H61', session_token=2023070)

# Get Historical data

itc_daily = bz.get_historical_data(
    interval='1day',
    from_date= "2022-08-15T07:00:00.000Z",
    to_date= "2022-11-18T07:00:00.000Z",
    stock_code="ITC",
    exchange_code="NSE",
    product_type="cash"
    )

pprint(itc_daily)

##### Subscribe to Live Data (websocket)

bz.ws_connect()

# bz.subscribe_feeds(
#     stock_code="ITC",
#     exchange_code="NSE",
#     product_type="cash"
# )

# def on_ticks(ticks):
#     # Callback to receive ticks
#     print("Ticks: {}".format(ticks))
#
# bz.on_ticks = on_ticks

bz.unsubscribe_feeds(stock_code="ITC",
    exchange_code="NSE",
    product_type="cash")
