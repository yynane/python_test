#!/usr/bin/env python
# encoding: utf-8

"""
@version: 3.5
@author: yuying
@file: test_math.py
@time: 2016/9/10 12:35
"""

import math


def quadratic(a, b, c):

    x_sqrt = b**2 - 4*a*c

    if x_sqrt < 0 or a == 0:
        return '无解'
    else:
        x1 = (-b + math.sqrt(x_sqrt)) / (2*a)
        x2 = (-b - math.sqrt(x_sqrt)) / (2*a)
        return x1, x2

print(quadratic(1, 6, 3,))
