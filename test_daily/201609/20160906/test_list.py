#!/usr/bin/env python
# encoding: utf-8

"""
@version: 3.5
@author: yuying
@file: test_list.py
@time: 2016/9/6 21:20
"""

test_list = [1, 2, 3, ]
print(test_list)

test_list.append(4)
print(test_list)

a = test_list.index(4)
print(a)

b = test_list.pop(0)
print(b)
print(test_list)

test_list.remove(2)
print(test_list)

test_list.reverse()
print(test_list)

test_list.extend([5, 6, ])
print(test_list)

test_list2 = [7, 8, ]
test_list.extend(test_list2)
print(test_list)
