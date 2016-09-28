#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 3.5
@author: yuying
@file: test_urlopen.py
@time: 2016/9/23 21:28
"""

import urllib.request

r = urllib.request.urlopen('http://douban.com')

html = r.read()

print(html)
