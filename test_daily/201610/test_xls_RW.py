#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 
@author: yuying
@file: test_xls_RW.py
@time: 2016/10/16 15:03
"""

import pandas

score = pandas.read_excel('score.xls')
score['sum'] = score['Python']+score['Math']
score.to_excel('score_sum.xlsx', sheet_name='scores')
