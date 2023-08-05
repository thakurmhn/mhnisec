#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 22:11:42 2023

@author: mohan
"""

from breeze_connect import BreezeConnect
from breeze_deploy.bzutils import BzUtils
import pandas as pd
import datetime as dt

from stocktrends import Renko


bzutils = BzUtils()


from_date_mo = dt.datetime.today() - dt.timedelta(days=30)
start_date_mo = from_date_mo.strftime("%Y-%m-%dT%H:%M:%S.000Z")
to_date_mo = dt.datetime.today()
end_date_mo = to_date_mo.strftime("%Y-%m-%dT%H:%M:%S.000Z")
timeframe_mo = '5minute'

from_date_yr = dt.datetime.today() - dt.timedelta(days=90)
start_date_yr = from_date_yr.strftime("%Y-%m-%dT%H:%M:%S.000Z")
to_date_yr = dt.datetime.today()
end_date_yr = to_date_yr.strftime("%Y-%m-%dT%H:%M:%S.000Z")
timeframe_yr = '30minute'


tickers = ['ITC', 'TCS', 'RELIND', 'ADAENT']
exchange = 'NSE'
segment = 'cash'

# creds dict
creds = bzutils.get_api_creds()
breeze = BreezeConnect(api_key=creds['api_key'])
breeze.generate_session(api_secret=creds['app_secret'],
                        session_token=creds['session_token'])

ohlc_data_5m = {}
ohlc_data_30m = {}
renko_data = {}
df_ohlc_5m = pd.DataFrame()
df_ohlc_30m = pd.DataFrame()


   
for ticker in tickers: 
    data_5m =  breeze.get_historical_data_v2(interval=timeframe_mo,
                                from_date=start_date_mo,
                                to_date=end_date_mo,
                                stock_code=ticker,
                                exchange_code=exchange,
                                product_type=segment)
    
    data_30m =  breeze.get_historical_data_v2(interval=timeframe_yr,
                                from_date=start_date_yr,
                                to_date=end_date_yr,
                                stock_code=ticker,
                                exchange_code=exchange,
                                product_type=segment)
    
       
    
    stock_data_5m = pd.DataFrame(data_5m['Success'])
    stock_data_5m.rename(columns={'datetime': 'date'}, inplace=True)
    stock_data_5m.dropna(how='any', inplace=True)
    df_ohlc_5m = stock_data_5m[['date', 'open', 'high', 'low', 'close', 'volume']]
    ohlc_data_5m[ticker] = df_ohlc_5m
    # ohlc_data_5m[ticker].set_index('date', inplace=True)
    
    
    stock_data_30m = pd.DataFrame(data_30m['Success'])
    stock_data_30m.rename(columns={'datetime': 'date'}, inplace=True)
    stock_data_30m.dropna(how='any', inplace=True)      
    df_ohlc_30m = stock_data_30m[['date', 'open', 'high', 'low', 'close', 'volume']]
    ohlc_data_30m[ticker] = df_ohlc_30m
    # ohlc_data_30m[ticker].set_index('datetime', inplace=True)
    

def ATR(DF, n=14):
    "function to calculate True Range and Average True Range"
    df = DF.copy()
    df["H-L"] = df["high"] - df["low"]
    df["H-PC"] = abs(df["high"] - df["close"].shift(1))
    df["L-PC"] = abs(df["low"] - df["close"].shift(1))
    df["TR"] = df[["H-L","H-PC","L-PC"]].max(axis=1, skipna=False)
    df["ATR"] = df["TR"].ewm(com=n, min_periods=n).mean()  # set com to span to match tradingview calculation
    return df["ATR"]


def renko_DF(DF, half_hr_df):
    "function to convert ohlc data into renko bricks"
    df = DF.copy()
# =============================================================================
#    # Commented as used with yfinance data, Close column not exist with isec  
#     df.reset_index(inplace=True)
#     df.drop("Close",axis=1,inplace=True)  
# =============================================================================
    df.columns = ["date","open","high","low","close", "volume"]
    df2 = Renko(df)
    # ATR * 3 = 120 # YOu can use your own ATR value
    # ATR is set to 14 period
    df2.brick_size = 3*round(ATR(half_hr_df,14).iloc[-1],0)
    renko_df = df2.get_ohlc_data() #if using older version of the library please use get_bricks() instead
    return renko_df

for ticker in ohlc_data_5m:
    renko_data[ticker] = renko_DF(ohlc_data_5m[ticker],ohlc_data_30m[ticker])