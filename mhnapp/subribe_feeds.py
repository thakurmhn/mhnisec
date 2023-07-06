from breeze_deploy.bzutils import BzUtils
from breeze_deploy.bzwsclient import WebSocketClient
from breeze_connect import BreezeConnect

bz = BzUtils()
# url = "https://livestream.icicidirect.com"
#
#
# breeze = BreezeConnect(api_key=bz.api_key)
# breeze.generate_session(api_secret=bz.app_secret,
#                         session_token=bz.session_token)
#
# ws_client = WebSocketClient(url)
# ws_client.connect()
# on_ticks_function = ws_client.get_on_ticks_function()
#
# print(breeze.subscribe_feeds(exchange_code='NSE', stock_code='TCS', get_exchange_quotes=True, get_market_depth=True))

bz.bz_websocket()


def on_ticks(self, ticks):
    print("{}".format(ticks))


bz.on_ticks = on_ticks
print(breeze.subscribe_feeds(exchange_code='NSE', stock_code='TCS', get_exchange_quotes=True, get_market_depth=True))