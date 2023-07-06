
from breeze_connect import BreezeConnect
import yaml

file = open('secret_token.yaml', 'r')
secret_dict = yaml.load(file, Loader=yaml.FullLoader)
app_key = secret_dict['api_key']
app_secret = secret_dict['app_secret']
app_session = secret_dict['session_token']

breeze = BreezeConnect(api_key=app_key)
breeze.generate_session(api_secret=app_secret,
                        session_token=app_session)
breeze.ws_connect()

data = None


def on_ticks(ticks):
    global data
    data = ticks
    #print("Ticks: {}".format(ticks))


breeze.on_ticks = on_ticks
breeze.subscribe_feeds(stock_token="37517")
#print(breeze.subscribe_feeds(exchange_code="NFO", stock_code="TCS", product_type="options", expiry_date="31-Aug-2023", strike_price="3200", right="Call", get_exchange_quotes=True, get_market_depth=False))

# breeze.subscribe_feeds(exchange_code="NFO", stock_code="TCS", product_type="options", expiry_date="31-Aug-2023", strike_price="3200", right="Call", get_exchange_quotes=True, get_market_depth=False)
print(data)
