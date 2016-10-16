#!/usr/bin/env python
# encoding: utf-8

"""
@version: 3.5
@author: yuying
@file: test_send_mail.py
@time: 2016/9/21 13:05
"""

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def send_mail(receiver):
    """邮件发送函数

        简单的邮件发送函数，后期可以通过增加参数优化。
    """

    ret = True  # 返回值，用于返回邮件是否发送成功。
    try:
        msg = MIMEText('邮件正文：Hello mail！', 'plain', 'utf-8')
        msg['From'] = formataddr(['test_from_mail', 'XXXX@139.com'])
        msg['To'] = formataddr(['tes_to_mail', receiver])
        msg['Subject'] = 'test_python'

        server = smtplib.SMTP('smtp.139.com', 25)
        server.login('XXXX@139.com', '密码')
        server.sendmail('13730847167@139.com', [receiver, ], msg.as_string())
        server.quit()
    except Exception:
        ret = False
    return ret

print(send_mail('XX@qq.com'))

