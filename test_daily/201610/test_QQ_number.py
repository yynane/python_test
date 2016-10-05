#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 
@author: yuying
@file: test_QQ_number.py
@time: 2016/10/5 11:20
"""

QQ_number = {'xiaoyun': 88888, 'xiaohong': 5555555, 'xiaoteng': 11111, 'xiaoyi': 1234321, 'xiaoyang': 1212121}


def input_name():

    global QQ_number

    name = input('Please enter the name:')
    while name not in QQ_number:
        name = input('Please enter the name again；If you want to quit, input q:')
        if name == 'q':
            break
    else:
        print(QQ_number[name])


def out_number():

    global QQ_number

    print('Who has the beautiful number:')
    for name, num in QQ_number.items():
        if num < 100000:
            print(name)


if __name__ == '__main__':
    input_name()
    out_number()
