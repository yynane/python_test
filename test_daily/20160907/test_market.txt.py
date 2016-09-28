#!/usr/bin/env python
# encoding: utf-8

"""
@version: 3.5
@author: yuying
@file: test_market.txt.py
@time: 2016/9/7 20:23
"""


def buy():  # 买操作
    global shopping_cart
    user_commodity = input('目前您的余额为%s元，请输入你需要的商品：' % balance)
    shopping_cart.append(user_commodity)


def add_sh_ca():  # 加入购物车
    global shopping_cart, balance

    balance = 100

    for i in shopping_cart:
        balance -= list_commodity.get(i)

    if balance >= 0:
        print('你目前的购物车中有：', shopping_cart)
        print('你目前的余额为：%s' % balance)
        return balance, shopping_cart
    else:
        print('你的余额不足，不能购买该物品。')
        shopping_cart.pop()
        print('你目前的购物车中有：', shopping_cart)
        print('因为你最后一次购物已经超过余额，故强制结账。')


# 程序开始
print('欢迎来到商城！')

list_commodity = {'牙膏': 15, '牙刷': 8, '毛巾': 32, '香皂': 12, '洗衣粉': 30, '面盆': 18, '杯子': 42, '台灯': 100, }
print('你能购买到的商品和价格如下：')
for commodity in list_commodity:
    print(commodity, list_commodity.get(commodity))

balance = 100
shopping_cart = []

while balance >= 0:
    buy()
    add_sh_ca()



