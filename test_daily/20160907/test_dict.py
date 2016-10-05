#!/usr/bin/env python
# encoding: utf-8

"""
@version: 3.5
@author: yuying
@file: test_dict.py
@time: 2016/9/7 16:41
"""


address_dict = {
    '北京': {
        '海淀': ('羊坊店', '甘家口', '紫竹院', '白下关', ),
        '朝阳': ('朝外', '建外', '呼家', '八里庄',)
    },
    '四川': {
        '成都': ('金牛', '青羊', '武侯', '成华', ),
        '绵阳': ('涪城区', '游仙区', '安州区', ),
        '宜宾': ('翠屏区', '高县', '宜宾', ),
    }

}

user_address = input('请输入你所在省份/直辖市：')

for address in address_dict:

    print(address)
    if user_address == address:
        print('你所在省份/直辖市有如下市/区：', address_dict.get(user_address))
        input('请输入你所在市/区')
        break
    else:
        print('没有你所输入的省份。')

'''
这串代码有问题，尚未完成。
'''


