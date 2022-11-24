from breeze_connect import BreezeConnect
from pprint import pprint

# First step is to generate session


# Get Historical data

isec_auth = BzAuth(api_key=app_creds['demo_app']['api_key'],
                       secret_key=app_creds['demo_app']['secret_key'],
                       )

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
