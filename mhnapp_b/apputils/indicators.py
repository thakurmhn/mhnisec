#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 11:14:45 2023

@author: mohan
"""

import numpy as np
import pandas as pd

def bollinger_bands(DF, n=14):
    "function to calculate Bollinger Band"
    df = DF.copy()
    df["MB"] = df["close"].rolling(n).mean()
    df["UB"] = df["MB"] + 2*df["close"].rolling(n).std(ddof=0)
    df["LB"] = df["MB"] - 2*df["close"].rolling(n).std(ddof=0)
    df["BB_Width"] = df["UB"] - df["LB"]
    return df[["MB","UB","LB","BB_Width"]]

def ATR(DF, n=14):
    "function to calculate True Range and Average True Range"
    df = DF.copy()
    df["H-L"] = df["high"] - df["low"]
    df["H-PC"] = abs(df["high"] - df["close"].shift(1))
    df["L-PC"] = abs(df["low"] - df["close"].shift(1))
    df["TR"] = df[["H-L","H-PC","L-PC"]].max(axis=1, skipna=False)
    df["ATR"] = df["TR"].ewm(com=n, min_periods=n).mean()  # set com to span to match tradingview calculation
    return df["ATR"]

def CAGR(DF):
    "function to calculate the Cumulative Annual Growth Rate of a trading strategy"
    df = DF.copy()
    df["return"] = DF["close"].pct_change()
    df["cum_return"] = (1 + df["return"]).cumprod()
    n = len(df)/252
    CAGR = (df["cum_return"].iloc[-1]) ** (1/n) -1
    return CAGR

def MACD(DF, a=12 ,b=26, c=9):
    """function to calculate MACD
       typical values a(fast moving average) = 12; 
                      b(slow moving average) =26; 
                      c(signal line ma window) =9"""
    df = DF.copy()
    df["ma_fast"] = df["close"].ewm(span=a, min_periods=a).mean()
    df["ma_slow"] = df["close"].ewm(span=b, min_periods=b).mean()
    df["macd"] = df["ma_fast"] - df["ma_slow"]
    df["signal"] = df["macd"].ewm(span=c, min_periods=c).mean()
    return df.loc[:,["macd","signal"]]

def max_dd(DF):
    "function to calculate max drawdown"
    df = DF.copy()
    df["return"] = df["close"].pct_change()
    df["cum_return"] = (1+df["return"]).cumprod()
    df["cum_roll_max"] = df["cum_return"].cummax()
    df["drawdown"] = df["cum_roll_max"] - df["cum_return"]
    return (df["drawdown"]/df["cum_roll_max"]).max()
    
def calmar(DF):
    "function to calculate calmar ratio"
    df = DF.copy()
    return CAGR(df)/max_dd(df)

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

def RSI(DF, n=14):
    "function to calculate RSI"
    df = DF.copy()
    df["change"] = df["close"] - df["close"].shift(1)
    df["gain"] = np.where(df["change"]>=0, df["change"], 0)
    df["loss"] = np.where(df["change"]<0, -1*df["change"], 0)
    df["avgGain"] = df["gain"].ewm(alpha=1/n, min_periods=n).mean()
    df["avgLoss"] = df["loss"].ewm(alpha=1/n, min_periods=n).mean()
    df["rs"] = df["avgGain"]/df["avgLoss"]
    df["rsi"] = 100 - (100/ (1 + df["rs"]))
    return df["rsi"]

