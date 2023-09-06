#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 11:44:20 2023

@author: mohan
"""

import pandas as pd
from apputils.isec_ohlcv import get_1day_ohlcv_df
from apputils.indicators import bollinger_bands
import datetime as dt

tickers=['ITC', 'TCS', 'RELIND', 'ADAENT']

daily_ohlcv_data = get_1day_ohlcv_df(days=365, tickers=tickers)

for ticker in daily_ohlcv_data:
    daily_ohlcv_data[ticker][["MB","UB","LB","BB_Width"]] = bollinger_bands(daily_ohlcv_data[ticker])
    
    