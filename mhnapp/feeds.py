from breeze_connect import BreezeConnect
import yaml
import time
from csvprocessor import CsvProcessor



file = open('secret_token.yaml', 'r')
secret_dict = yaml.load(file, Loader=yaml.FullLoader)
app_key = secret_dict['api_key']
app_secret = secret_dict['app_secret']
app_session = secret_dict['session_token']

breeze = BreezeConnect(api_key=app_key)
breeze.generate_session(api_secret=app_secret,
                        session_token=app_session)
breeze.ws_connect()

for tick in ticks:
        # Process tick data based on conditions
        if tick['price'] > 100:
            print("High-priced tick:", tick)
        else:
            print("Low-priced tick:", tick)

breeze.on_ticks = on_ticks


csvproc = CsvProcessor()
stock_codes = csvproc.get_icici_stock_codes()

for stock_token in stock_codes:
    breeze.subscribe_feeds(stock_token=stock_token)

# Wait for data to be received
time.sleep(5)
