#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2019/4/10 上午10:36 
# @Author : zhubc 
# @File : settings.py 
# @Software: PyCharm


def get_db_uri(dbinfo):
    ENGINE = dbinfo.get("ENGINE", "mysql")
    DRIVER = dbinfo.get("DRIVER", "pymysql")
    HOST = dbinfo.get("HOST", "127.0.0.1")
    PORT = dbinfo.get("PORT", "3306")
    USERNAME = dbinfo.get("USERNAME", "root")
    PASSWD = dbinfo.get("PASSWD", "123456")
    NAME = dbinfo.get("NAME", "test")
    return "{}+{}:{}:{}@{}:{}/{}".format(ENGINE, DRIVER, USERNAME, PASSWD, HOST, PORT, NAME)


class Config:
    # api_id = '557c656d71f54a7e8f8c681d7a9ab006'
    # api_secret = '7ff1e984d75b48f9b3ba3aa3033ad252'

    api_id = '5cd6813423b84eb09080d0c01b1279fd'
    api_secret = 'a8534cf01c2744949588362599d716b9'


class TestingConfig(Config):
    """测试环境"""
    url = 'http://100.73.18.124:19641'
    expired_data = {'api_id': 'c34192cd19954c6fa5c6d88ae430bf8f',
                    'api_secret': '1b3dbf40d9564506bd958cbc65d63c3e'}
    no_permission_data = {'api_id': '227ea6c642d54c499f0f5e3b0a0f3736',
                          'api_secret': '2021bef56a634ac081ac0d0d2f7462f5'}
    quota_data = {'api_id': '8f6f11910017423f975959334c1d59c4',
                  'api_secret': '09085e248fdb42e4b9cf80c8c0173538'}

    DATABASE = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USERNAME": "root",
        "PASSWD": "123456",
        "HOST": "127.0.0.1",
        "PORT": "3306",
        "NAME": "Person"
    }

    DATABASE_URI = get_db_uri(DATABASE)


class DemoConfig(Config):
    """灰度环境"""
    url = 'http://cloudapijavastage.linkface.cn'
    expired_data = {'api_id': 'c0af780788cb4bf9ae55f498a917d91c',
                    'api_secret': '9cc4ba335f2e4c508d59015cffa57063'}
    no_permission_data = {'api_id': '7011a19784674c8a81d07b4b68b1d8a5',
                          'api_secret': '99d9ad7a70884c37ba0116d18993c3ee'}
    quota_data = {'api_id': '759438bd7f8e4d758ddd0fc3b75ded86',
                  'api_secret': 'a9621cf404f2404abb63fbf4d489ec20'}


class ProductionConfig(Config):
    """正式环境"""
    url = 'https://cloudapi.linkface.cn'
    expired_data = {'api_id': 'c0af780788cb4bf9ae55f498a917d91c',
                    'api_secret': '9cc4ba335f2e4c508d59015cffa57063'}
    no_permission_data = {'api_id': '7011a19784674c8a81d07b4b68b1d8a5',
                          'api_secret': '99d9ad7a70884c37ba0116d18993c3ee'}
    quota_data = {'api_id': '759438bd7f8e4d758ddd0fc3b75ded86',
                  'api_secret': 'a9621cf404f2404abb63fbf4d489ec20'}


envs = {
    "default": DemoConfig
}
