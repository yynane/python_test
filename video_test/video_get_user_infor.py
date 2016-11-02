#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 
@author: yuying
@file: video_get_user_infor.py
@time: 2016/10/30 11:28
"""
import csv
import subprocess


def get_user_info(v, ms=13730847167, user_path_data="user.csv"):

    user_data_file = open(user_path_data, "ab")
    user_data = csv.writer(user_data_file)

    if ms in v[4]:
        user_data.writero(v)

    user_data_file.close()


if __name__ == '__main__':

    cmd1 = subprocess.getstatusoutput('ls -1 /data/xdr/old/*.csv')[1]
    csv_list = cmd1.split("\n")

    for v in csv_list:
        get_user_info(v)
