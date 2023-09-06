#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 14:28:29 2023

@author: mohan
"""

import pandas as pd
from apputils.isec_ohlcv import get_5min_ohlcv_df
from apputils.indicators import ATR
from apputils.indicators import RSI
from apputils.indicators import MACD

tickers=['ITC', 'TCS', 'RELIND', 'ADAENT']

ohlcv_data = get_5min_ohlcv_df(days=1, tickers=tickers)

for ticker in ohlcv_data:
    ohlcv_data[ticker]["ATR"] = ATR(ohlcv_data[ticker])
    ohlcv_data[ticker]["RSI"] = RSI(ohlcv_data[ticker])
    ohlcv_data[ticker][["MACD","SIGNAL"]] = MACD(ohlcv_data[ticker], a=12 ,b=26, c=9)