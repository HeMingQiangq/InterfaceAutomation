#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time, sys, os
base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(base_dir, 'interface'))
sys.path.append(os.path.join(base_dir, 'db_fixture'))
from HTMLTestRunner import HTMLTestRunner
from unittest import defaultTestLoader
from email.mime.text import MIMEText
from email.header import Header
import smtplib
# from db_fixture import test_data


# ====================定义发送邮件====================
def send_email(file_new):
    with open(file_new, 'rb') as f:
        mail_body = f.read()

    msg_from = 'zhubc@linkface.cn'  # 发送方邮箱
    passwd = '123'  # 发送方邮箱的授权码
    msg_to = 'zhubc@linkface.cn'  # 收件人邮箱
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['From'] = msg_from
    msg['To'] = msg_to
    msg['Subject'] = Header("自动化测试报告", 'utf-8')
    try:
        smtp = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
        smtp.login(msg_from, passwd)
        smtp.sendmail(msg_from, msg_to, msg.as_string())
        print('email has send out !')
    except Exception as e:
        print("发送失败：%s" % e)
    finally:
        smtp.quit()


# ======查找测试报告目录，找到最新生成的测试报告文件=======
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new


# 指定测试用例为当前文件夹下的 interface 目录
test_dir = os.path.join(base_dir, 'interface')
testsuit = defaultTestLoader.discover(test_dir, pattern='*result_1_test.py')


if __name__ == "__main__":
    # test_data.init_data() # 初始化接口测试数据

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = os.path.join(base_dir, 'report/' + now + '_result.html')
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner(stream=fp,
                                title='linkface接口自动化测试报告',
                                description='''
                                运行环境:Python3, Requests, unittest；
                                java测试环境地址:http://100.73.18.123:19641；
                                ruby测试环境地址:http://100.66.225.5:10006''')
        runner.run(testsuit)
    # file_path = new_report('./report/')   # 查找新生成的报告
    # send_email(file_path)   # 调用发邮件模块
