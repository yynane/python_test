#!/usr/bin/env python
# encoding: utf-8

"""
@version: 3.5
@author: yuying
@file: test_is_37_ture.py
@time: 2016/9/21 21:13
"""

# 验证命题：如果一个三位整数是37的倍数，则这个整数循环左移后得到的另两个3位数也是37的倍数。
# 注意验证命题的结果输出方式，只要输出命题为真还是假即可，而非每一个三位数都有一个真假的输出


def move(arg, count=1):
    """
    将数字的最左边位，移至最右边
    :param arg: 需要转换的数据，将首字母移至末尾。
    :param count: 需要转换的次数。
    :return:转换后的数据。
    """
    arg_list = list(str(arg))  # 将数字转化为列表（中间先转为字符串）。
    for x in range(count):  # 将数字移动。
        temp = arg_list.pop(0)
        arg_list.append(temp)
    arg_move = int(''.join(arg_list))  # 移动后，再还原为整数型数字。
    return arg_move


def is_true():
    """
    判断命题是否成立。
    :return: 成立返回True，失败返回False。
    """
    for i in range(100, 1000):
        if i % 37 == 0:
            if move(i) % 37 == 0:
                if move(i, 2) % 37 == 0:
                    pass
                else:
                    return False
    return True

print(is_true())


