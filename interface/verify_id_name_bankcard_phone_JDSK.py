#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2019/07/12 上午11:03
# @Author : hemq
# @File : verify_id_name_bankcard_phone--银行卡四要素对接-京东数科
# @Software: PyCharm

import unittest
import requests
import os, sys
import time
import csv
from client import *

# from requests_toolbelt import MultipartEncoder
pack_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(pack_dir)
data_dir = os.path.join(pack_dir, "pictureDatas/bankcard/")
from datetime import datetime


class verify_id_name_bankcard_phone_jdsk(unittest.TestCase):
    '''verify_id_name_bankcard_phone--银行卡四要素对接-京东数科'''

    @classmethod
    def setUpClass(cls):
        # cls.__url = "https://cloudapi.linkface.cn/data/verify_id_name_bankcard_phone" # 线上地址
        # cls.__url = "http://cloudapijavastage.linkface.cn/data/verify_id_name_bankcard_phone"  # 灰度地址
        cls.__url = "http://100.73.18.123:19641/data/verify_id_name_bankcard_phone"  # 测试地址
        cls.__wrongurl = "http://cloudapijavastage.linkface.cn//data/verify_id_name_bankcard_pho" # 错误地址
        # cls.__url = r'http://122.115.42.100/'
        # cls.__url = r'https://cloudapi.linkface.cn/'
        # cls.__url = r'http://100.66.225.5:10006/'
        # cls.__url = r"https://cloudapi.linkface.cn/data/verify_id_name_bankcard_phone_acclevel"  # 线上地址
        cls.__now = time.strftime("%Y-%m-%d %H_%M_%S")
        cls.__path = pack_dir + '/result/' + cls.__now + '_result.csv'
        cls.expired_data = {"api_id": "c34192cd19954c6fa5c6d88ae430bf8f",
                            "api_secret": "1b3dbf40d9564506bd958cbc65d63c3e"}
        cls.no_permission_data = {"api_id": "227ea6c642d54c499f0f5e3b0a0f3736",
                                  "api_secret": "2021bef56a634ac081ac0d0d2f7462f5"}
        cls.quota_data = {"api_id": "8f6f11910017423f975959334c1d59c4",
                          "api_secret": "09085e248fdb42e4b9cf80c8c0173538"}
        # cls.expired_data = {'api_id': 'c0af780788cb4bf9ae55f498a917d91c',
        #                     'api_secret': '9cc4ba335f2e4c508d59015cffa57063'}
        # cls.no_permission_data = {'api_id': '7011a19784674c8a81d07b4b68b1d8a5',
        #                           'api_secret': '99d9ad7a70884c37ba0116d18993c3ee'}
        # cls.quota_data = {'api_id': '759438bd7f8e4d758ddd0fc3b75ded86',
        #                 'api_secret': 'a9621cf404f2404abb63fbf4d489ec20'}
        print("初始化数据完成。")

    @classmethod
    def tearDownClass(cls):
        print()
        print("All cases finished.")

    def setUp(self):
        self.client = Client(url=self.__url, method=Method.POST, type=Type.FORM_FILE)
        self.__data = {'api_id': '',
                       'api_secret': '',
                       'name': '',
                       'id_number': '',
                       'card_number': '',
                       'phone_number': '',
                       }
        # self.__file = {'file': open(data_dir + '/正常人像照.jpg', 'rb')}
        # self.__file = {
        #     'selfie_file': open(data_dir + '/正常人脸照片.jpg', 'rb'),
        #     'watermark_picture_file': open(data_dir + '/正常水印照片.jpg', 'rb')
        # }

        self.start = datetime.now()
        print(self.start)
        print('##############test start###############')

    def tearDown(self):
        self.end = datetime.now()
        print((self.end - self.start).seconds)
        print('##############test end###############')

    def test_01apiid_wrong(self):
        '''api_id错误，UNAUTHORIZED，401'''
        self.__data['api_id'] = '557c656d71f54a7e8f8c681d7a9ab00'
        client = self.client
        client.set_data(self.__data)
        # client.set_files(self.__file)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(401)
        client.check_dict_equal({'request_id': 'request_id', 'status': 'UNAUTHORIZED'})

    def test_02apiid_null(self):
        '''api_id为空，UNAUTHORIZED，401'''
        self.__data['api_id'] = ''
        client = self.client
        client.set_data(self.__data)
        # client.set_files(self.__file)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(401)
        client.check_dict_equal({'request_id': 'request_id', 'status': 'UNAUTHORIZED'})

    def test_03apiid_miss(self):
        '''缺少api_id，UNAUTHORIZED，401'''
        self.__data.pop('api_id')
        client = self.client
        client.set_data(self.__data)
        # client.set_files(self.__file)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(401)
        client.check_dict_equal({'request_id': 'request_id', 'status': 'UNAUTHORIZED'})

    def test_04apisecret_wrong(self):
        '''api_secret错误，UNAUTHORIZED，401'''
        self.__data['api_secret'] = '7ff1e984d75b48f9b3ba3aa3033ad252a'
        client = self.client
        client.set_data(self.__data)
        # client.set_files(self.__file)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(401)
        client.check_dict_equal({'request_id': 'request_id', 'status': 'UNAUTHORIZED'})

    def test_05apisecret_null(self):
        '''api_secret为空，UNAUTHORIZED，401'''
        self.__data['api_secret'] = ''
        client = self.client
        client.set_data(self.__data)
        # client.set_files(self.__file)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(401)
        client.check_dict_equal({'request_id': 'request_id', 'status': 'UNAUTHORIZED'})

    def test_06apisecret_miss(self):
        '''缺少api_secret，UNAUTHORIZED，401'''
        self.__data.pop('api_secret')
        client = self.client
        client.set_data(self.__data)
        # client.set_files(self.__file)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(401)
        client.check_dict_equal({'request_id': 'request_id', 'status': 'UNAUTHORIZED'})

    def test_07key_expired(self):
        '''KEY_EXPIRED，401'''
        client = self.client
        client.set_data(self.expired_data)
        # client.set_files(self.__file)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(401)
        client.check_dict_equal({'request_id': 'request_id',
                                 'reason': 'key expired at 2018-07-02T23:59:59+08:00',
                                 'status': 'KEY_EXPIRED'})  # 2018-07-02T23:59:59+08:00;2018-12-07T23:59:59+08:00

    def test_08no_permission(self):
        '''NO_PERMISSION，403'''
        data = self.no_permission_data
        client = self.client
        client.set_data(data)
        # client.set_files(self.__file)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(403)
        client.check_dict_equal({'request_id': 'request_id', 'status': 'NO_PERMISSION'})

    def test_09out_of_quota(self):
        '''OUT_OF_QUOTA，403'''
        data = self.quota_data
        client = self.client
        client.set_data(data)
        # client.set_files(self.__file)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(403)
        client.check_dict_equal({'request_id': 'request_id', 'status': 'OUT_OF_QUOTA'})

    def test_10_passTest(self):
        '''正常四要素'''
        data = self.__data
        client = self.client
        client.set_data(data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(200)
        client.check_dict_equal({
            "status": "OK",
            "request_id": "request_id",
            "result": 1
        })

    def test_11_namempty(self):
        ''' name 参数值为空'''
        self.__data['name'] = ''
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "argument 'name': blank string",
            "request_id": "request_id"
        })

    def test_12_nameDeletion(self):
        ''' name 字段不传'''
        del (self.__data['name'])
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "argument 'name': not found",
            "request_id": "request_id"
        })

    def test_13_nameWrong(self):
        ''' name 字段值错误'''
        self.__data['name'] = '张坚果'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(200)
        client.check_dict_equal({
            "status": "OK",
            "request_id": "request_id",
            "result": 2
        })

    def test_14_nameIncludeetter(self):
        ''' name 参数值为包含字母'''
        self.__data['name'] = '张坚vvv'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Input parameter error",
            "request_id": "request_id"
        })

    def test_15_nameIncludeNum(self):
        ''' name 参数值为包含数字'''
        self.__data['name'] = 121
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Input parameter error",
            "request_id": "request_id"
        })

    def test_16_nameIncludelank(self):
        ''' name 参数值为包含空格'''
        self.__data['name'] = '张 坚'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Input parameter error",
            "request_id": "request_id"
        })

    def test_17_nameIncludeSpecialharacter(self):
        ''' name 参数值为包含特殊字符'''
        self.__data['name'] = '#$#$#$#$#$'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Input parameter error",
            "request_id": "request_id"
        })

    def test_18_nameIncludeEtterAndNum(self):
        ''' name 参数值为包含字母+数字'''
        self.__data['name'] = 'xsxs1314'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Input parameter error",
            "request_id": "request_id"
        })

    def test_19_nameIncludeEtterAndBlank(self):
        ''' name 参数值为包含字母+空格'''
        self.__data['name'] = 'xs  xs'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Input parameter error",
            "request_id": "request_id"
        })

    def test_20_nameIncludeEtterAndSpecialharacter(self):
        ''' name 参数值为包含字母+特殊字符'''
        self.__data['name'] = 'xs@#￥%%ss'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Input parameter error",
            "request_id": "request_id"
        })

    def test_21_nameIncludeNumAndBlank(self):
        ''' name 参数值为包含数字+空格'''
        self.__data['name'] = '1312  '
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Input parameter error",
            "request_id": "request_id"
        })

    def test_22_nameIncludeNumAndSpecialharacter(self):
        ''' name 参数值为包含数字+特殊字符'''
        self.__data['name'] = '1312@#￥%%ss'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Input parameter error",
            "request_id": "request_id"
        })

    def test_23_nameIncludeBlankAndSpecialharacter(self):
        ''' name 参数值为包含空格+特殊字符'''
        self.__data['name'] = '  @#￥  %%ss'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Input parameter error",
            "request_id": "request_id"
        })

    def test_24_nameIncludeNumAndEtterAndBlank(self):
        ''' name 参数值为包含数字+字母+空格'''
        self.__data['name'] = '12  xbsh  34'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Input parameter error",
            "request_id": "request_id"
        })

    def test_25_nameIncludeNumAndEtterAndBlank(self):
        ''' name 参数值为包含数字+字母+空格'''
        self.__data['name'] = '12  xbsh  34'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Input parameter error",
            "request_id": "request_id"
        })

    def test_26_nameIncludeNumAndEtterAndSpecialharacter(self):
        ''' name 参数值为包含数字+字母+特殊符号'''
        self.__data['name'] = '12xsxs#￥%'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Input parameter error",
            "request_id": "request_id"
        })

    def test_27_nameIncludeEtterAndBlankAndSpecialharacter(self):
        ''' name 参数值为包含字母+空格+特殊符号'''
        self.__data['name'] = 'xsxs  #$%^&...'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Input parameter error",
            "request_id": "request_id"
        })

    def test_28_nameIncludeNumAndEtterAndBlankAndSpecialharacter(self):
        ''' name 参数值为包含数字+字母+空格+特殊符号'''
        self.__data['name'] = '1314xsxs  #$%^&...'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Input parameter error",
            "request_id": "request_id"
        })

    def test_28_nameIncludetrue(self):
        ''' name 参数值为true'''
        self.__data['name'] = True
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Input parameter error",
            "request_id": "request_id"
        })

    def test_29_nameIncludefalse(self):
        ''' name 参数值为false'''
        self.__data['name'] = False
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Input parameter error",
            "request_id": "request_id"
        })

    def test_30_idNumbermpty(self):
        ''' id_number 参数值为空'''
        self.__data['id_number'] = ''
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "argument 'id_number': blank string",
            "request_id": "request_id"
        })

    def test_31_idNumberDeletion(self):
        ''' id_number 字段不传'''
        del (self.__data['id_number'])
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "argument 'id_number': not found",
            "request_id": "request_id"
        })

    def test_32_idNumberWrong(self):
        ''' id_number 字段值错误'''
        self.__data['id_number'] = '522524196708253214'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(200)
        client.check_dict_equal({
            "status": "OK",
            "request_id": "request_id",
            "result": 2
        })

    def test_33_idNumberIncludeSpecialharacter(self):
        ''' id_number 字段包含特殊字符'''
        self.__data['id_number'] = '####，，，，，'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Invalid id_number",
            "request_id": "request_id"
        })

    def test_34_idNumberMax(self):
        ''' id_number 字段值长度超过18位'''
        self.__data['id_number'] = '441230197602070473456789'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Invalid id_number",
            "request_id": "request_id"
        })

    def test_35_idNumberMin(self):
        ''' id_number 字段值长度不超过18位'''
        self.__data['id_number'] = '441230197602'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Invalid id_number",
            "request_id": "request_id"
        })

    def test_36_idNumberIncludeNum(self):
        ''' id_number 字段值传num'''
        self.__data['id_number'] = 610302197709194514
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(200)
        client.check_dict_equal({
            "status": "OK",
            "request_id": "request_id",
            "result": 1
        })

    def test_37_idNumberIncludeTrue(self):
        ''' id_number 字段值传true'''
        self.__data['id_number'] = True
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Invalid id_number",
            "request_id": "request_id"
        })

    def test_38_idNumberIncludeFalse(self):
        ''' id_number 字段值传false'''
        self.__data['id_number'] = False
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Invalid id_number",
            "request_id": "request_id"
        })

    def test_39_idNumberIncludeEtter(self):
        ''' id_number 字段值传字母'''
        self.__data['id_number'] = 'ssssss'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Invalid id_number",
            "request_id": "request_id"
        })

    def test_40_cardNumbermpty(self):
        ''' cardNumber 参数值为空'''
        self.__data['card_number'] = ''
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "argument 'card_number': blank string",
            "request_id": "request_id"
        })

    def test_41_cardNumberDeletion(self):
        ''' cardNumber 字段不传'''
        del (self.__data['card_number'])
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "argument 'card_number': not found",
            "request_id": "request_id"
        })

    def test_42_cardNumberIncludeEtter(self):
        ''' cardNumber 字段包含字母'''
        self.__data['card_number'] = 'xbshbxhsbxhsbxhs'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Invalid card_number",
            "request_id": "request_id"
        })

    def test_43_cardNumberIncludeBlank(self):
        ''' cardNumber 字段包含空格'''
        self.__data['card_number'] = '621793386693874  9'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Invalid card_number",
            "request_id": "request_id"
        })

    def test_44_cardNumberIncludeSpecialharacter(self):
        ''' cardNumber 字段包含特殊字符'''
        self.__data['card_number'] = '#$%,;'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Invalid card_number",
            "request_id": "request_id"
        })

    def test_45_cardNumberIncludeEtterAndBlank(self):
        ''' cardNumber 字段包含字母+空格'''
        self.__data['card_number'] = 'sss cdcd'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Invalid card_number",
            "request_id": "request_id"
        })

    def test_46_cardNumberIncludeEtterAndSpecialharacter(self):
        ''' cardNumber 字段包含字母+特殊字符'''
        self.__data['card_number'] = 'xsxs#￥%……&*'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Invalid card_number",
            "request_id": "request_id"
        })

    def test_47_cardNumberIncludeBlankAndSpecialharacter(self):
        ''' cardNumber 字段包含空格+特殊字符'''
        self.__data['card_number'] = '   ￥%……&*'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Invalid card_number",
            "request_id": "request_id"
        })

    def test_48_phoneNumbermpty(self):
        ''' phoneNumber 参数值为空'''
        self.__data['phone_number'] = ''
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "argument 'phone_number': blank string",
            "request_id": "request_id"
        })

    def test_49_phoneNumberDeletion(self):
        ''' phoneNumber 字段不传'''
        del (self.__data['phone_number'])
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "argument 'phone_number': not found",
            "request_id": "request_id"
        })

    def test_50_phoneNumberMax(self):
        ''' phoneNumber 长度超过11位'''
        self.__data['phone_number'] = '1356094426678799'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Invalid phone_number",
            "request_id": "request_id"
        })

    def test_51_phoneNumberMax(self):
        ''' phoneNumber 长度不超过11位'''
        self.__data['phone_number'] = '13560'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Invalid phone_number",
            "request_id": "request_id"
        })

    def test_52_phoneNumberIncludeEtter(self):
        ''' phoneNumber 字段包含字母'''
        self.__data['phone_number'] = 'xbshbxhsbxhsbxhs'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Invalid phone_number",
            "request_id": "request_id"
        })

    def test_53_phoneNumberIncludeBlank(self):
        ''' phoneNumber 字段包含空格'''
        self.__data['phone_number'] = '        '
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Invalid phone_number",
            "request_id": "request_id"
        })

    def test_54_phoneNumberIncludeSpecialharacter(self):
        ''' phoneNumber 字段包含特殊字符'''
        self.__data['phone_number'] = '#$%,;'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Invalid phone_number",
            "request_id": "request_id"
        })

    def test_55_phoneNumberIncludeEtterAndBlank(self):
        ''' phoneNumber 字段包含字母+空格'''
        self.__data['phone_number'] = 'sss cdcd'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Invalid phone_number",
            "request_id": "request_id"
        })

    def test_56_phoneNumberIncludeEtterAndSpecialharacter(self):
        ''' phoneNumber 字段包含字母+特殊字符'''
        self.__data['phone_number'] = 'xsxs#￥%……&*'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Invalid phone_number",
            "request_id": "request_id"
        })

    def test_57_phoneNumberIncludeBlankAndSpecialharacter(self):
        ''' phoneNumber 字段包含空格+特殊字符'''
        self.__data['phone_number'] = '   ￥%……&*'
        client = self.client
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(400)
        client.check_dict_equal({
            "status": "INVALID_ARGUMENT",
            "reason": "Invalid phone_number",
            "request_id": "request_id"
        })

    def test_58_wrongUrl(self):
        ''' 错误的url'''
        wrongClient = Client(url=self.__wrongurl, method=Method.POST, type=Type.FORM_FILE)
        client = wrongClient
        client.set_data(self.__data)
        client.send()
        client.write_to_csv(self.__path)
        client.check_status_code(404)
        client.check_dict_equal({
            "request_id": "request_id",
            "status": "NOT_FOUND"
        })


if __name__ == '__main__':
    unittest.main()
