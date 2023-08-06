#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 18:38:42 2023

@author: mohan
"""

from nsepy import get_history
from datetime import date
data = get_history(symbol="SBIN", start=date(2021,1,1), end=date(2023,7,31))
data[['Close']].plot()


from nsetools import Nse

nse = Nse()

print(nse)

nse.get_preopen_nifty()

