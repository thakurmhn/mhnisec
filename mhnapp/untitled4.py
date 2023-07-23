#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 20:18:18 2023

@author: mohan
"""
import datetime as dt


from_date = dt.datetime.today() - dt.timedelta(3650)
start_date = from_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
to_date = dt.datetime.today()
end_date = to_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")




