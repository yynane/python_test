#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 3.5
@author: yuying
@file: test_work_countchar.py
@time: 2016/9/25 16:17
"""

"""
统计字符串中的字符个数。
定义函数countchar()统计字符串中所有出现的字母的个数（允许输入大写字符，并且计数时不区分大小写）。
"""


def countchar(str_a):

    list_count = [0 for x in range(26)]
    list_letters = list('abcdefghijklmnopqrstuvwxyz')
    for i, j in enumerate(list_letters):
        if j in str_a:
            list_count[i] = str_a.count(j)
    return list_count

if __name__ == "__main__":
    print(countchar(input().lower()))


