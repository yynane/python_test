#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 3.5
@author: yuying
@file: test_get_url.py
@time: 2016/10/4 15:57
"""

import urllib.request

"""
“http://tieba.baidu.com/p/1000000000”至“http://tieba.baidu.com/p/1000000009”这10个页面；
以1000000000.html~1000000009.html这样的文件名保存到本地硬盘上
"""

for i in range(10):

    page = 1000000000 + i
    html_open = urllib.request.urlopen('http://tieba.baidu.com/p/%s' % page)
    html_read = html_open.read()
    html_file = open('%s.html' % page, 'wb')
    html_file.write(html_read)
    html_file.close()
    html_open.close()
