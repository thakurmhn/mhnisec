from breeze_deploy.breeze_auth import BzAuth

bzconn = BzAuth._conn_to_live_data()

itc_daily = bz.get_historical_data()
    interval='1day',
    from_date= "2022-08-15T07:00:00.000Z",
    to_date= "2022-11-18T07:00:00.000Z",
    stock_code="ITC",
    exchange_code="NSE",
    product_type="cash"
    )

pprint(itc_daily)