#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 3.5
@author: yuying
@file: test_file_BITW.py
@time: 2016/9/25 13:38
"""
"""
(1) 创建一个文件Blowing in the wind.txt，其内容是：
How many roads must a man walk down
Before they call him a man
How many seas must a white dove sail
Before she sleeps in the sand
How many times must the cannon balls fly
Before they're forever banned
The answer my friend is blowing in the wind
The answer is blowing in the wind
(2) 在文件头部插入歌名“Blowin’ in the wind”
(3) 在歌名后插入歌手名“Bob Dylan”
(4) 在文件末尾加上字符串“ 1962 by Warner Bros. Inc.”
(5) 在屏幕上打印文件内容
"""

file_BITW = open('Blowing in the wind.txt', 'w+', encoding='utf-8')
file_BITW.write("""How many roads must a man walk down
Before they call him a man
How many seas must a white dove sail
Before she sleeps in the sand
How many times must the cannon balls fly
Before they're forever banned
The answer my friend is blowing in the wind
The answer is blowing in the wind\n
""")
# 上面为第一个要求，写一个歌词文件。

file_BITW.seek(0)                                                   # 将文件指针移到文件开头。
list_BITW = file_BITW.readlines()                                   # 将以前的文字读到一个列表中。

list_BITW.insert(0, 'Blowin’ in the wind')                          # 在有原来内容的列表中添加数据。
list_BITW.insert(1, '\t By:Bob Dylan\n\n')
list_BITW.append('1962 by Warner Bros. Inc.')

file_BITW.seek(0)
file_BITW.writelines(list_BITW)                                     # 将列表写入文件。
file_BITW.close()

