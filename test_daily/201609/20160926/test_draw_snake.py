#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 3.5
@author: yuying
@file: test_draw_snake.py
@time: 2016/9/26 20:01
"""

"""
绘制一条蛇
"""

import turtle


def draw_snake(rad, angle, s_len, neckrad):
    for i in range(s_len):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1, 180)
    turtle.fd(rad*2/3)


def main1():
    turtle.setup(1360,800,0,0)
    pythonsize = 10
    turtle.pensize(pythonsize)
    turtle.pencolor("blue")
    turtle.seth(-40)
    draw_snake(40,80, 5,pythonsize/2)

if __name__ == "__main__":
    main1()