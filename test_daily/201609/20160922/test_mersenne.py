#!/usr/bin/env python
# encoding: utf-8

"""
@version: 3.5
@author: yuying
@file: test_mersenne.py
@time: 2016/9/22 22:07
"""

'''
题目内容：找第n个默尼森数。P是素数且M也是素数，并且满足等式M=2**P-1，则称M为默尼森数。
例如，P=5，M=2**P-1=31，5和31都是素数，因此31是默尼森数。
'''


def prime(num):
    """
    判断输入的num是否为素数。
    :param num: 需要判断的数。
    :return: 素数为True,否则为False。
    """
    prime_no = [2]
    if num == 1 or num == 2:
        return True
    elif num <= 0:
        return False
    else:
        for i in range(2, num+1):
            if i not in prime_no:
                for j in prime_no:
                    if i % j == 0:
                        break
                else:
                    prime_no.append(i)
        if num in prime_no:
            return True
        else:
            return False


def monisen(no):
    """
    取第no个莫尼森数。
    """

    no_int = int(no)    # 将输入的字符串转换为整型。
    monisen_list = []   # 存储莫尼森数的列表。

    for i in range(2, 100):
        if prime(i):
            m = 2 ** i - 1
            if prime(m):
                monisen_list.append(m)
                if len(monisen_list) == no_int: # 如果已经取到第no个莫尼森数，则跳出循环，以免暂用太多内存。
                    break

    return monisen_list[no_int - 1]

print(monisen(input()))
