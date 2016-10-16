#!/usr/bin/env python
# encoding: utf-8

"""
@version: 3.5
@author: yuying
@file: test_foo.py
@time: 2016/9/16 15:31
"""

print(7 % 2)


def foo(num, base):
    if num >= base:
        foo(num/base, base)
    print(num % base)

foo(126, 2)
