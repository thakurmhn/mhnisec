from breeze_deploy.breeze_auth import BzAuth
from pprint import pprint

app_creds = BzAuth._get_api_creds()

isec_auth = BzAuth(api_key=app_creds['demo_app']['api_key'],
                       secret_key=app_creds['demo_app']['secret_key'],
                       )

bz = isec_auth._isec_login()
# Demo historical data

itc_daily = bz.get_historical_data(
    interval='1day',
    from_date= "2022-08-15T07:00:00.000Z",
    to_date= "2022-11-18T07:00:00.000Z",
    stock_code="ITC",
    exchange_code="NSE",
    product_type="cash"
    )

pprint(itc_daily)