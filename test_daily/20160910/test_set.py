#!/usr/bin/env python
# encoding: utf-8

"""
@version: 3.5
@author: yuying
@file: test_set.py
@time: 2016/9/10 12:17
"""


set_1 = {1, 2, 3, 4, }
set_2 = {3, 4, 5, 6, }
set_s_d = set_1.symmetric_difference(set_2)
set_d = set_1.difference(set_2)

print('set_1:', type(set_1), set_1)
print('set_1:', type(set_2), set_2)
print('S1和S2的symmetric_difference:', set_s_d)
print('S1和S2的difference', set_d)

'''
运行结果
set_1: <class 'set'> {1, 2, 3, 4}
set_1: <class 'set'> {3, 4, 5, 6}
S1和S2的symmetric_difference: {1, 2, 5, 6}
S1和S2的difference {1, 2}
'''