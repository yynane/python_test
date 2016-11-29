#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 
@author: yuying
@file: data_merge.py
@time: 2016/11/17 14:39
"""

import subprocess
import csv

cmd1 = subprocess.getstatusoutput(r'dir .\data /b')[1]
file_list = cmd1.splitlines()
open_csv = open(r'.\data\all.csv', 'w', newline='')
file_all = csv.writer(open_csv)

for i in file_list:
    file_csv = open(r'.\data\%s' % i, 'r')
    for v in csv.reader(file_csv):
        if "city_id" not in v[0]:
            print(v)
            file_all.writerow(v)
    file_csv.close()

open_csv.close()


