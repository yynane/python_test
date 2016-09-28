#!/usr/bin/env python
# encoding: utf-8

"""
@version: 3.5
@author: yuying
@file: test_tuple.py
@time: 2016/9/6 21:05
"""

a = 1
b = 2

tuple_test = (a, b)

print(tuple_test)

a = 10
b = 20

print(tuple_test)

tuple_test = (a, b)

print(tuple_test)

'''该test测试结果如下：
测试元祖能否用变量赋值。
测试结果为元祖能用变量赋值，但是赋值之后，变量值变了，元祖中元素的值不会变。除非重新给原则赋值。
(1, 2)
(1, 2)
(10, 20)
下面列表的情况和元祖一直。
说明：在元祖和列表中，通过变量给予赋值，元祖/列表是被指向变量的空间，而不是变量本省，变量变了，元祖/列表的值不会变。
如同 a = 20 ; b = a ; a = 10 。最终b还是20。
'''

a = 'list1'
b = 'list2'

list_test = [a, b]

print(list_test)

a = 'list10'
b = 'list20'

print(list_test)

list_test = [a, b]

print(list_test)
