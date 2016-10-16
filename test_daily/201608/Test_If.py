#!/usr/bin/env python
# encoding: utf-8

"""
@version: 3.5
@author: yuying
@time: 2016/8/29 10:58
"""

import random

lucky_number = random.randint(0, 100)


def first_way():
    """这是第一种方式：

        1、用while循环；
        2、有循环计数变量；
        3、在while语句外定义guess_number变量。
    """

    global lucky_number
    guess_number = int("0")
    loop_count = 0

    while guess_number != lucky_number and loop_count < 5:
        guess_number = int(input("Input Number:"))
        if guess_number == lucky_number:
            print("You Are Right!")
            break
        elif loop_count == 2:
            print("Your Are Fail!")
            break
        elif guess_number > lucky_number:
            print("Your input number to big")
            loop_count += 1
        elif guess_number < lucky_number:
            print("Your input number to small")
            loop_count += 1


def second_way():
    """这是第二种实现方式：

        1、用while循环；
        2、有计数变量；
        3、guess_number在while内部；
        4、增加running变量判断是否猜正确，其实可以在方法一的判断更好。
    """

    global lucky_number
    running = True
    loop_count = 0

    while running and loop_count < 5:
        guess_number = int(input("Input Number:"))
        if guess_number == lucky_number:
            print("You Are Right!")
            running = False
        elif loop_count == 2:
            print("Your Are Fail!")
            break
        elif guess_number > lucky_number:
            print("Your input number to big")
            loop_count += 1
        elif guess_number < lucky_number:
            print("Your input number to small")
            loop_count += 1


def third_way():
    """这是第三种实现方式：

        1、用for循环；
        2、无单独定义计数变量；
        3、guess_number在for内部；最优解。
    """

    global lucky_number

    for i in range(5):
        guess_number = int(input("Input Number:"))
        if guess_number == lucky_number:
            print("You Are Right!")
            break
        elif i == 4:
            print("Your Are Fail!")
            break
        elif guess_number > lucky_number:
            print("Your input number to big")
        elif guess_number < lucky_number:
            print("Your input number to small")


third_way()


