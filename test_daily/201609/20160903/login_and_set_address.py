#!/usr/bin/env python
# encoding: utf-8

"""
@version: 3.5
@author: yuying
@file: login_and_set_address.py
@time: 2016/9/3 15:26
"""
"""
作业：
让用户输入用户名和密码；校验三次，三次未成功，则锁定用户。
登录成功之后，让用户选择地址，地址有三级菜单供用户选择。
"""


def login1():
    """自己实现登录验证的方法：

       纯粹自己根据已学的东西想的方法。缺点是：用户名密码只能存储一个。
    """

    user_info_file = open('user_info.txt', 'r')  # 用户名和密码存储文件
    user_info_list = user_info_file.readlines()  # 正确的用户名和密码存储队列
    username = user_info_list[0].strip()  # 正确的用户名
    password = user_info_list[1]  # 正确的密码
    user_info_file.close()

    for i in range(3):

        username_input = input('请输出用户名:')
        password_input = input('请输入密码:')
        login_count = 2-i  # 判断还能输入多少次。
        lock_user_file = open('lock_user.txt', 'r')  # 黑名单

        for line in lock_user_file.readlines():
            if line.strip() == username_input:
                print('用户不能登录，请联系管理员解除锁定。')
                return False

        else:
            if username == username_input and password == password_input:
                print('登录成功')
                return True
            elif i == 2:
                lock_user_file_add_user = open('lock_user.txt','a')
                lock_user_file_add_user.write('\n')
                lock_user_file_add_user.write(username_input)
                lock_user_file_add_user.close()
                print('登录次数超过限制，用户已经被锁定。')
                return False
            else:
                print('用户名或密码错误，你还能尝试登录',login_count,'次。')

        lock_user_file.close()


def login2():
    """综合视频教材修改后的方法，优化的地方：

        1、使用with语句打开文件，避免close文件。
        2、可以分割一行中不同的内容，每行可以存一个用户信息。
    """

    user_info_file = 'user_info.txt'  # 用户名和密码存储文件
    lock_user_file = 'lock_user.txt'  # 黑名单文件

    for i in range(3):

        username_input = input('请输出用户名:')
        login_count = 2-i  # 判断还能输入多少次。

        with open(lock_user_file, 'r') as lock_user:  # 判断用户是否在黑名单，在黑名单则跳出，函数反馈False。
            for line in lock_user.readlines():
                if line.strip() == username_input:
                    print('用户不能登录，请联系管理员解除锁定。')
                    return False

        password_input = input('请输入密码:')

        with open(user_info_file, 'r') as user_info:  # 判断用户是否登录成功，登录成功则跳出，函数反馈True。
            for line in user_info.readlines():
                username, password = line.strip().split()
                if username == username_input and password == password_input:
                    print('登录成功')
                    return True

        if i == 2:  # 如果用户输入错误三次，则加入黑名单，并跳出，函数反馈False。
            lock_user_file_add_user = open(lock_user_file, 'a')
            lock_user_file_add_user.write('\n'+username_input)
            lock_user_file_add_user.close()
            print('登录次数超过限制，用户已经被锁定。')
            return False
        else:
            print('用户名或密码错误，你还能尝试登录', login_count, '次。')

'''
def write_address():

    address_list_file = open('address_list.txt', 'r', encoding='utf-8')  #地址列表
    address_list = address_list_file.readlines()
    names = locals()

    for i in range(len(address_list)):
        names['address_list_detail' + str(i)] = address_list[i]
        print(address_list_detail + str(i))

# province_list



write_address()

'''



