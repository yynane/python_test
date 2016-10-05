#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 
@author: yuying
@file: test_login_dict.py
@time: 2016/10/5 10:10
"""

"""
use dict to updata user information
"""

user = {'user1': 'dqw123', 'user2': 'faf765'}


def new_users():

    global user

    username = input('Please enter the register username:')
    if username in user:
        print('The username has been used.')
    else:
        password = input('Please enter the password:')
        user[username] = password
        print('Register succeed, you can login.')


def old_users():

    global user

    username = input('Please enter the login username:')
    if username not in user:
        print('The username enter error, without this user.')
    else:
        password = input('Please enter the password:')
        if user[username] == password:
            print('Login succeed.')
        else:
            print('Login failed.')


def login():

    class_login = int(input('Register input 1, login input 2:'))
    if class_login == 1:
        new_users()
        old_users()
    elif class_login == 2:
        old_users()
    else:
        print('Enter error.')

if __name__ == '__main__':
    login()