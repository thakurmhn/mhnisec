#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 13:55:05 2023

@author: mohan
"""

import pandas as pd
from apputils.isec_ohlcv import get_1day_ohlcv_df
from apputils.indicators import ATR
from apputils.indicators import RSI

tickers=['ITC', 'TCS', 'RELIND', 'ADAENT']

daily_ohlcv_data = get_1day_ohlcv_df(days=365, tickers=tickers)

for ticker in daily_ohlcv_data:
    daily_ohlcv_data[ticker]["ATR"] = ATR(daily_ohlcv_data[ticker])
    daily_ohlcv_data[ticker]["RSI"] = RSI(daily_ohlcv_data[ticker])