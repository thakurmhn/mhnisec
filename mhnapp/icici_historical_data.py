#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 19:08:33 2023

@author: mohan
"""

from breeze_connect import BreezeConnect
from breeze_deploy.bzutils import BzUtils
import pandas as pd

bzutils = BzUtils()

# start date
def start_date():
    
    # Need to be updated as required
    s_month = 7
    s_day = "Monday"
    s_date = 11
    s_time = "07:00:00"
    s_iso_date = bzutils.get_datetime_iso(month=s_month,
                                  day=s_day, date=s_date, time=s_time)
    
    return s_iso_date

# end date

def end_date():
     
    # Need to be updated as required 
    e_month = 7
    e_day = "Monday"
    e_date = 11
    e_time = "18:00:00"
    
    e_iso_date = bzutils.get_datetime_iso(month=e_month, day=e_day,
                                  date=e_date, time=e_time)
    return e_iso_date
    
from_date = start_date()
to_date = end_date()

timeframe = '5minute'
stock_code = 'NIITEC'
exchange = 'NSE'
segment = 'cash'

# creds dict
creds = bzutils.get_api_creds()
breeze = BreezeConnect(api_key=creds['api_key'])
breeze.generate_session(api_secret=creds['app_secret'],
                        session_token=creds['session_token'])



# Get data

data = breeze.get_historical_data_v2(interval=timeframe,
                            from_date=from_date,
                            to_date=to_date,
                            stock_code=stock_code,
                            exchange_code=exchange,
                            product_type=segment)



# Store data in Dataframe
stock_data = pd.DataFrame(data['Success'])

# extract columns from stockdata Dataframe
# Create a blank Dataframe
ohlc_data = pd.DataFrame()
ohlc_data = stock_data[['datetime', 'open', 'high', 'low', 'close']]
ohlc_data.set_index('datetime', inplace=True)
