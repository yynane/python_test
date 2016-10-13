#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 3.5
@author: yuying
@file: test_class.py
@time: 2016/10/12 20:37
"""


class ClassA:
    attr_a = 1

obj_a = ClassA()
ClassA.attr_a = 2
print(ClassA.attr_a, obj_a.attr_a)


class ClassB:
    attr_b = 1

obj_b_1 = ClassB()
obj_b_2 = ClassB()
obj_b_3 = ClassB()
obj_b_1.attr_b = 3
ClassB.attr_b = 4
obj_b_3.attr_c = 5
print(ClassB.attr_b, obj_b_1.attr_b, obj_b_2.attr_b, obj_b_3.attr_c)
# 结果是 4 ， 3 ，4 ，5。
del obj_b_1.attr_b
print(obj_b_1.attr_b)
# del之前是3，del之后恢复原来的类的值，结果是4。


'''
结论：
1、（第16行）实例会继承类的属性（attr_a），类属性值变更时，实例会随之变更。
2、（第26行）实例重新定义了一个属性，名字和类的属性一致，优先级高于类的属性，结果为3。
3、（第27行）类的属性变了，obj_b_2属性attr_b的值改变，因为它没新定义同名属性，而obj_b_1的属性attr_b的值，不会变。
4、（第31行）删除了实例的属性之后，将调用类的属性。
'''