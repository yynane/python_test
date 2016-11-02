#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 
@author: yuying
@file: acl_examine.py
@time: 2016/11/2 10:52
"""

import subprocess

cmd1 = subprocess.getstatusoutput(r'dir .\acl /b')[1]
file_list = cmd1.splitlines()
key_word = [' host host_', ' filter ', ' filter-group', ' cbb-id ', ' charge-property ', ' category-group ', ' l7-info ', ' l7-info-group ', ' l7-rule ', ' rule ', ' rule-enrichment ', ' rule-binding ']


def host_comparison(line):
    pass


for i in file_list:
    file_cfg = open(r'.\acl\%s' % i, 'r')
    file_format = open(r'.\acl\%s.txt' % i, 'w')
    for j in file_cfg.readlines():
        for k in key_word:
            if k in j[:20]:
                file_format.writelines(j)
    file_cfg.close()
    file_format.close()

