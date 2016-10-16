#!/usr/bin/env python
# encoding: utf-8

"""
@version: 3.5
@author: yuying
@file: test_prime_No.py
@time: 2016/9/22 19:50
"""

'''
找出2-100直接的素数并输出
'''


prime_no = [2]

for i in range(2, 101):
    if i not in prime_no:
        for j in prime_no:
            if i % j == 0:
                break
        else:
            prime_no.append(i)

print(prime_no)










