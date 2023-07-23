#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 15:00:21 2023

@author: mohan
"""

from breeze_connect import BreezeConnect
from breeze_deploy.bzutils import BzUtils
import pandas as pd
import datetime as dt


bzutils = BzUtils()


from_date = dt.datetime.today() - dt.timedelta(days=20)
start_date = from_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
to_date = dt.datetime.today()
end_date = to_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")

timeframe = '30minute'
# tickers = ['ITC', 'TCS', 'RELIND', 'ADAENT']
tickers = ["ITC"]
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
    
def Boll_Band(DF, n=14):
    "function to calculate Bollinger Band"
    df = DF.copy()
    df["MB"] = df["close"].rolling(n).mean()
    df["UB"] = df["MB"] + 2*df["close"].rolling(n).std(ddof=0)
    df["LB"] = df["MB"] - 2*df["close"].rolling(n).std(ddof=0)
    df["BB_Width"] = df["UB"] - df["LB"]
    return df[["MB","UB","LB","BB_Width"]]

for ticker in ohlc_data:
    ohlc_data[ticker][["MB","UB","LB","BB_Width"]] = Boll_Band(ohlc_data[ticker])
    
    