#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 
@author: yuying
@file: test_homework_yahoo.py
@time: 2016/10/15 16:33
"""

from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date
import pandas as pd

today = date.today()
start = (today.year-2, today.month, today.day)
quotes = quotes_historical_yahoo_ochl('MSFT', start, today)
attributes = ['date', 'open', 'close', 'high', 'low', 'volume']
quotesdf = pd.DataFrame(quotes, columns=attributes)

list1 = []
for i in range(0, len(quotes)):
    x = date.fromordinal(int(quotes[i][0]))
    y = date.strftime(x, '%Y/%m/%d')
    list1.append(y)
quotesdf.index = list1
quotesdf = quotesdf.drop(['date'], axis = 1 )
print(quotesdf)

# list2 = []
# tmpdf = quotesdf['15/01/01':'15/12/31']
# for i in range(0, len(tmpdf)):
#     list2.append(int(tmpdf.index[i][3:5]))
# tmpdf['month'] = list2
# print(tmpdf[tmpdf.close > tmpdf.open]['month'].value_counts())
