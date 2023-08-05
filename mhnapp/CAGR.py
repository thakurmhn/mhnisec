#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 13:56:43 2023

@author: mohan
"""
from breeze_connect import BreezeConnect
from breeze_deploy.bzutils import BzUtils
import pandas as pd
import datetime as dt

bzutils = BzUtils()

from_date = dt.datetime.today() - dt.timedelta(days=252)
start_date = from_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
to_date = dt.datetime.today()
end_date = to_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")

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
    
def CAGR(DF):
    "function to calculate the Cumulative Annual Growth Rate of a trading strategy"
    df = DF.copy()
    df["return"] = DF["close"].pct_change()
    df["cum_return"] = (1 + df["return"]).cumprod()
    n = len(df)/252
    CAGR = (df["cum_return"].iloc[-1]) ** (1/n) -1
    return CAGR


for ticker in ohlc_data:
    print("CAGR of {} = {}".format(ticker,CAGR(ohlc_data[ticker])))
