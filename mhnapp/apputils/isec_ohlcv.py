#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 08:22:03 2023

@author: mohan
"""

from breeze_connect import BreezeConnect
from breeze_deploy.bzutils import BzUtils
import pandas as pd
import datetime as dt


bzutils = BzUtils()


def get_1day_ohlcv_df(days=365, tickers=list()):
    "Returns 1 day OHLC Dataframe"

    from_date = dt.datetime.today() - dt.timedelta(days=days)
    start_date = from_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    to_date = dt.datetime.today()
    end_date = to_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    
    timeframe = '1day'
    # tickers = ['ITC', 'TCS', 'RELIND', 'ADAENT']
    tickers = tickers
    exchange = 'NSE'
    segment = 'cash'
    
    # creds dict
    creds = bzutils.get_api_creds()
    breeze = BreezeConnect(api_key=creds['api_key'])
    breeze.generate_session(api_secret=creds['app_secret'],
                            session_token=creds['session_token'])
    
    ohlc_data = {}
    df_ohlc = pd.DataFrame()
    
    daily_data = {}
       
    for ticker in tickers: 
        data =  breeze.get_historical_data_v2(interval=timeframe,
                                    from_date=start_date,
                                    to_date=end_date,
                                    stock_code=ticker,
                                    exchange_code=exchange,
                                    product_type=segment)
           
        
        stock_data = pd.DataFrame(data['Success'])
        stock_data.dropna(how='any', inplace=True)      
        df_ohlc = stock_data[['datetime','open', 'high', 'low', 'close', 'volume']]
        df_ohlc.rename(columns={'datetime': 'date'}, inplace=True)
        
        ohlc_data[ticker] = df_ohlc
        daily_data[ticker] = df_ohlc
        
    # Returns daily historical data df    
    return daily_data


def get_1min_ohlcv_df(days=30, tickers=list()):
    "Returns 1 minute OHLC Dataframe"

    from_date = dt.datetime.today() - dt.timedelta(days=days)
    start_date = from_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    to_date = dt.datetime.today()
    end_date = to_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    
    timeframe = '1minute'
    # tickers = ['ITC', 'TCS', 'RELIND', 'ADAENT']
    tickers = tickers
    exchange = 'NSE'
    segment = 'cash'
    
    # creds dict
    creds = bzutils.get_api_creds()
    breeze = BreezeConnect(api_key=creds['api_key'])
    breeze.generate_session(api_secret=creds['app_secret'],
                            session_token=creds['session_token'])
    
    ohlc_data = {}
    df_ohlc = pd.DataFrame()
    
    one_min_data = {}
       
    for ticker in tickers: 
        data =  breeze.get_historical_data_v2(interval=timeframe,
                                    from_date=start_date,
                                    to_date=end_date,
                                    stock_code=ticker,
                                    exchange_code=exchange,
                                    product_type=segment)
           
        
        stock_data = pd.DataFrame(data['Success'])
        stock_data.dropna(how='any', inplace=True)      
        df_ohlc = stock_data[['datetime','open', 'high', 'low', 'close', 'volume']]
        df_ohlc.rename(columns={'datetime': 'date'}, inplace=True)
        
        ohlc_data[ticker] = df_ohlc
        one_min_data[ticker] = df_ohlc
        
    # Returns daily historical data df    
    return one_min_data


def get_5min_ohlcv_df(days=30, tickers=list()):
    "Returns 5 minute OHLC Dataframe"

    from_date = dt.datetime.today() - dt.timedelta(days=days)
    start_date = from_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    to_date = dt.datetime.today()
    end_date = to_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    
    timeframe = '5minute'
    # tickers = ['ITC', 'TCS', 'RELIND', 'ADAENT']
    tickers = tickers
    exchange = 'NSE'
    segment = 'cash'
    
    # creds dict
    creds = bzutils.get_api_creds()
    breeze = BreezeConnect(api_key=creds['api_key'])
    breeze.generate_session(api_secret=creds['app_secret'],
                            session_token=creds['session_token'])
    
    ohlc_data = {}
    df_ohlc = pd.DataFrame()
    
    five_min_data = {}
       
    for ticker in tickers: 
        data =  breeze.get_historical_data_v2(interval=timeframe,
                                    from_date=start_date,
                                    to_date=end_date,
                                    stock_code=ticker,
                                    exchange_code=exchange,
                                    product_type=segment)
           
        
        stock_data = pd.DataFrame(data['Success'])
        stock_data.dropna(how='any', inplace=True)      
        df_ohlc = stock_data[['datetime','open', 'high', 'low', 'close', 'volume']]
        df_ohlc.rename(columns={'datetime': 'date'}, inplace=True)
        
        ohlc_data[ticker] = df_ohlc
        five_min_data[ticker] = df_ohlc
        
    # Returns daily historical data df    
    return five_min_data


def get_30min_ohlcv_df(days=30, tickers=list()):
    "Returns 30 minute OHLC Dataframe"

    from_date = dt.datetime.today() - dt.timedelta(days=days)
    start_date = from_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    to_date = dt.datetime.today()
    end_date = to_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    
    timeframe = '30minute'
    # tickers = ['ITC', 'TCS', 'RELIND', 'ADAENT']
    tickers = tickers
    exchange = 'NSE'
    segment = 'cash'
    
    # creds dict
    creds = bzutils.get_api_creds()
    breeze = BreezeConnect(api_key=creds['api_key'])
    breeze.generate_session(api_secret=creds['app_secret'],
                            session_token=creds['session_token'])
    
    ohlc_data = {}
    df_ohlc = pd.DataFrame()
    
    thirty_min_data = {}
       
    for ticker in tickers: 
        data =  breeze.get_historical_data_v2(interval=timeframe,
                                    from_date=start_date,
                                    to_date=end_date,
                                    stock_code=ticker,
                                    exchange_code=exchange,
                                    product_type=segment)
           
        
        stock_data = pd.DataFrame(data['Success'])
        stock_data.dropna(how='any', inplace=True)      
        df_ohlc = stock_data[['datetime','open', 'high', 'low', 'close', 'volume']]
        df_ohlc.rename(columns={'datetime': 'date'}, inplace=True)
                      
        ohlc_data[ticker] = df_ohlc
        thirty_min_data[ticker] = df_ohlc
        
    # Returns daily historical data df    
    return thirty_min_data


if __name__ == '__main__':
    
    daily_df = get_1day_ohlcv_df(tickers=['ITC', 'TCS', 'RELIND', 'ADAENT'])
    
    onemin_df = get_1min_ohlcv_df(tickers=['ITC', 'TCS', 'RELIND', 'ADAENT'])
        
    fivemin_df = get_5min_ohlcv_df(tickers=['ITC', 'TCS', 'RELIND', 'ADAENT'])
    
    thirty_min_df = get_30min_ohlcv_df(tickers=['ITC', 'TCS', 'RELIND', 'ADAENT'])



