#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 17:59:13 2023

@author: mohan

How to use Dataframe.plot() to draw plots
"""

from breeze_connect import BreezeConnect
from breeze_deploy.bzutils import BzUtils
import pandas as pd
import datetime as dt


bzutils = BzUtils()


from_date = dt.datetime.today() - dt.timedelta(days=3650)
start_date = from_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
to_date = dt.datetime.today()
end_date = to_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")

timeframe = '1day'
tickers = ['ITC', 'TCS', 'RELIND']
exchange = 'NSE'
segment = 'cash'

# creds dict
creds = bzutils.get_api_creds()
breeze = BreezeConnect(api_key=creds['api_key'])
breeze.generate_session(api_secret=creds['app_secret'],
                        session_token=creds['session_token'])

cl_prices = pd.DataFrame()

   
for ticker in tickers: 
    data =  breeze.get_historical_data_v2(interval=timeframe,
                                from_date=start_date,
                                to_date=end_date,
                                stock_code=ticker,
                                exchange_code=exchange,
                                product_type=segment)
       
    
    stock_data = pd.DataFrame(data["Success"])
    
    cl_prices[ticker] = stock_data['close']


cl_prices.set_index(stock_data['datetime'], inplace=True)
cl_prices.dropna(axis=0, how='any', inplace=True)
daily_return = cl_prices.pct_change()

cl_prices.plot()
cl_prices.plot(subplots=True, layout = (2,2), title = "Stock Price Evolution", grid =True) # Subplots of the stocks

#plotting daily returns and cumulative returns    
daily_return.plot()
(1+daily_return).cumprod().plot(title = "Stock Price Evolution", grid =True)