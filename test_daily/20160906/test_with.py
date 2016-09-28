#!/usr/bin/env python
# encoding: utf-8

"""
@version: 3.5
@author: yuying
@file: test_with.py.py
@time: 2016/9/6 20:48
"""

with open('test.txt', 'w') as test:

    for i in range(3):

        test.write(str(i) + '\n')

    for i in range(3):

        test.write(str(i) + 'D\n')

with open('test.txt', 'a') as test:

    for i in range(3):

        test.write(str(i) + 'S\n')

'''
该with测试：通过with，写数据到文件，是追加还是替换。
'''