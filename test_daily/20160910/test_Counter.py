#!/usr/bin/env python
# encoding: utf-8

"""
@version: 3.5
@author: yuying
@file: test_Counter.py
@time: 2016/9/10 17:18
"""

import collections

count = collections.Counter('Elements are counted from an iterable or initialized from another mapping.')
print(count)

count2 = collections.Counter({'red': 4, 'blue': 2})
print(count2)


for item in count:
    print(item)

for item in count.values():
    print(item)

for item in count.items():
    print(item)

for k, v in count.items():
    print(k, v)
