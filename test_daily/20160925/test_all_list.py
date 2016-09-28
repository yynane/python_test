#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 3.5
@author: yuying
@file: test_all_list.py
@time: 2016/9/25 10:58
"""
"""
测试列表所有的特性和方法。
"""


# test1：用表达式创建列表。

list_test_1 = [x*5 for x in range(1, 21)]
# print(list_test_1)
list_test_1_B = [x for x in range(5, 105, 5)]
# print(list_test_1_B)
list_test_1_C = [(x+1, y+1) for x in range(0, 100, 2) for y in range(1, 100, 2)]
# print(list_test_1_C)

# test2：算整数型列表平均值。

list_test_2 = list_test_1
# print(sum(list_test_2)/len(list_test_2))

# test3：扩展列表，并枚举列表。

list_test_3 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
list_test_3_B = ['Saturday', 'Sunday']
list_test_3.extend(list_test_3_B)   # 改变原来的列表。
# print(list_test_3)
# for i, j in enumerate(list_test_3):
#     print(i+1, j)

# test4:sort排序练习。

list_test_4 = list_test_1
list_test_4.sort(reverse=True)      # 改变原来的列表。
# print(list_test_4)
# print(sorted(list_test_4))          # 未改变原来的列表，返回一个改变后的列表。The list not changed.
# print(list_test_4)


list_test_4_B = list_test_3
list_test_4_B.sort(key=len)
# print(list_test_4_B)











