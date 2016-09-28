#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 3.5
@author: yuying
@file: test_hanoi.py
@time: 2016/9/23 13:44
"""


'''
实现汉诺塔的移动顺序。
'''


def hanoi(n, x, y, z):
    if n == 1:
        print(x, '-->', z)
    else:
        hanoi(n-1, x, z, y)     # 将前n-1个盘子从x移动到y上
        hanoi(1, x, y, z)       # 将最底下的最后一个盘子从x移动到z上
        hanoi(n-1, y, x, z)     # 将y上的n-1个盘子移动到z上

no = int(input('请输入汉诺塔的层数：'))

hanoi(no, 'x', 'y', 'z')
