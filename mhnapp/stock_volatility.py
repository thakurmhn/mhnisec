#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 20:44:31 2023

@author: mohan
"""

from breeze_connect import BreezeConnect
from breeze_deploy.bzutils import BzUtils
import pandas as pd
import datetime as dt
import numpy as np

bzutils = BzUtils()


from_date = dt.datetime.today() - dt.timedelta(days=252)
start_date = from_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
to_date = dt.datetime.today()
end_date = to_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")

#timeframe = '1day'
timeframe = '30minute'
tickers = ['ITC', 'TCS', 'RELIND', 'ADAENT']
exchange = 'NSE'
segment = 'cash'

# creds dict
creds = bzutils.get_api_creds()
breeze = BreezeConnect(api_key=creds['api_key'])
breeze.generate_session(api_secret=creds['app_secret'],
                        session_token=creds['session_token'])

ohlc_data = {}
df_ohlc = pd.DataFrame()
   
for ticker in tickers: 
    data =  breeze.get_historical_data_v2(interval=timeframe,
                                from_date=start_date,
                                to_date=end_date,
                                stock_code=ticker,
                                exchange_code=exchange,
                                product_type=segment)
       
    
    stock_data = pd.DataFrame(data['Success'])
    stock_data.dropna(how='any', inplace=True)      
    df_ohlc = stock_data[['open', 'high', 'low', 'close', 'volume']]
    ohlc_data[ticker] = df_ohlc
    
def volatility(DF):
    "function to calculate annualized volatility of a trading strategy"
    df = DF.copy()
    df["daily_ret"] = DF["close"].pct_change()
    vol = df["daily_ret"].std() * np.sqrt(252)
    return vol

for ticker in ohlc_data:
    print("vol for {} = {}".format(ticker,volatility(ohlc_data[ticker])))