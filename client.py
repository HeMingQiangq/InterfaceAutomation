#import pandas

import requests
import hashlib
import unittest
import jsonpath
import util
import sys
import pymysql
import os
import json
import csv


base_dir = os.path.dirname(os.path.abspath(__file__))


class Method:
    POST = 'POST'
    GET = 'GET'


class Type:
    FORM_FILE = 0
    URL_ENCODE = 1
    FORM = 2
    JSON = 3
    XML = 4
    FILE = 5


class DATABASE:
    # xml驱动版本
    # re = util.read_config(base_dir + '/config.xml', './/config/database/*')
    # HOST = re.get('host')
    # USER = re.get('user')
    # PASSWORD = re.get('password')
    # NAME = re.get('db')

    # excel驱动版本
    re = util.read_config_excel(base_dir + '/excel_cases/case_template.xlsx', '数据库配置')
    data = re.get('数据库配置')
    if data:
        HOST = data[0].get('地址')
        USER = data[0].get('用户名')
        PASSWORD = data[0].get('密码')
        NAME = data[0].get('数据库')

# xml驱动版本
# DATA = util.read_config(sys.argv[0] + '/../config.xml', './/config/data/*')


# excel驱动版本,获取全局数据sheet内容
data = util.read_config_excel(base_dir + '/excel_cases/case_template.xlsx', '全局数据').get('全局数据')
DATA = {}
if data:
    for d in data:
        DATA[d.get('变量名')] = d.get('变量值')


class Client(unittest.TestCase):

    VALUES = {}

    def __init__(self, url, method, type=0):
        self.__url = url
        self.__method = method
        self.__headers = {}
        self.__type = type
        self.__data = {}
        self.__file = {}
        self.__res = None
        self._type_equality_funcs = {}

    def add(func):
        '''装饰器，用于打印断言成功信息或者断言失败抛出异常'''
        def wrapper(self, first, second, msg=None):
            try:
                func(self, first, second, msg)
                print('检查点成功。\n实际结果：[{first}]\n预期结果：[{second}]'.format(first=first, second=second))
            except AssertionError:
                raise AssertionError()
        return wrapper

    def set_headers(self, headers):
        """设置请求头"""
        if isinstance(headers, dict):
            self.__headers = headers
        else:
            raise Exception('headers类型为字典')

    def set_files(self, file):
        """设置入参文件"""
        if isinstance(file, dict):
            self.__file = file
        elif file == '' or file is None:
            self.__file = {}
        else:
            raise Exception('file类型为字典')

    def set_data(self, data):
        """设置请求体"""
        if isinstance(data, dict):
            if self.__type == 1:
                self.__headers['Content-type'] = 'application/x-www-form-urlencoded'
            elif self.__type == 0 or self.__type == 2 or self.__type == 5:
                pass
            elif self.__type == 3:
                self.__headers['Content-type'] = 'application/json'
            elif self.__type == 4:
                self.__headers['Content-type'] = 'text/xml'
            # elif self.__type == 0:
            #     raise Exception('未设置请求正文类型，无法传递正文内容')
            else:
                raise Exception('请求正文类型不存在')
            self.__data = data
        else:
            raise Exception('data类型为字典，如果为xml正文：{"xml": xml字符串}')

    def send(self):
        """发送http请求"""
        if self.__method == 'GET':
            self.__res = requests.get(url=self.__url, params=self.__data, headers=self.__headers)
        elif self.__method == 'POST':
            if self.__type == 0:
                self.__res = requests.post(url=self.__url, data=self.__data, headers=self.__headers, files=self.__file,
                                           verify=False)
            else:
                if self.__type == 1 or self.__type == 2:
                    self.__res = requests.post(url=self.__url, data=self.__data, headers=self.__headers, verify=False)
                elif self.__type == 3:
                    self.__res = requests.post(url=self.__url, json=self.__data, headers=self.__headers, verify=False)
                elif self.__type == 4:
                    xml_str = self.__data.get('xml')
                    if xml_str and isinstance(xml_str, str):
                        self.__res = requests.post(url=self.__url, data=xml_str, headers=self.__headers, verify=False)
                    else:
                        raise Exception('xml正文的请求，请正确添加xml字符串')
                elif self.__type == 5:
                    self.__res = requests.post(url=self.__url, files=self.__data, headers=self.__headers, verify=False)
        else:
            raise Exception('不支持的请求方法类型')

    def add_sign(self, token):
        list = []
        for k, v in self.__data.items():
            if k != 'username':
                list.append('%s=%s' % (k, v))
        list.sort()
        sign_str = "%spara=%s" % (token, '&'.join(list))
        md5 = hashlib.md5()
        md5.update(sign_str.encode(encoding="utf-8"))
        sign = md5.hexdigest()
        self.__data['sign'] = sign

    # 获取请求数据和响应数据
    @property
    def url(self):
        return self.__url

    @property
    def method(self):
        return self.__method

    @property
    def type(self):
        return self.__type

    @property
    def text(self):
        if self.__res.status_code:
            return self.__res.text
        else:
            return None

    @property
    def status_code(self):
        if self.__res.status_code:
            return self.__res.status_code
        else:
            return None

    @property
    def response_time(self):
        if self.__res.status_code:
            return self.__res.elapsed.total_seconds()
        else:
            return None

    @property
    def res_cookies(self):
        if self.__res.status_code:
            return requests.utils.dict_from_cookiejar(self.__res.cookies)
        else:
            return None

    @property
    def res_headers(self):
        if self.__res.status_code:
            return self.__res.headers
        else:
            return None

    @property
    def res_time(self):
        if self.__res.status_code:
            return round(self.__res.elapsed.total_seconds()*1000)
        else:
            return None

    def res_to_json(self):
        if self.__res.status_code:
            try:
                return self.__res.json()
            except:
                return None
        else:
            return None

    # 封装检查点
    def check_status_code(self, status=200):
        if self.__res.status_code:
            self.assertEqual(self.__res.status_code, status,
                             '响应状态码错误。实际结果：[{first}]'.format(first=str(self.__res.status_code)))
            print('检查点成功。实际结果：[{first}]，预期结果：[{second}]'.format(first=self.__res.status_code, second=status))
        else:
            self.assertTrue(False, '无法获取相应状态码:' + str(self.__res.json()))

    @add
    def check_equal(self, first, second, msg=None):
        self.assertEqual(first, second, msg=msg)

    @add
    def check_not_equal(self, first, second, msg=None):
        self.assertNotEqual(first, second, msg=msg)

    def json_value(self, path):
        if self.__res.status_code:
            object = jsonpath.jsonpath(self.res_to_json(), path)
            if object:
                return object[0]
        return None

    def json_values(self, path):
        if self.__res.status_code:
            object = jsonpath.jsonpath(self.res_to_json(), path)
            if object:
                return object
        return None

    def check_jsonNode_equal(self, path, exp, msg=None):
        node = self.json_value(path)
        self.assertEqual(node, exp, msg)
        print('检查点成功。实际结果：[{first}]，预期结果：[{second}]'.format(first=node, second=exp))

    def check_dict_equal(self, path):
        if self.__res.json():
            res = self.__res.json()
            if res.get('request_id') and res.get('image_id') and res.get('person_uuid'):
                res['request_id'] = 'request_id'
                res['image_id'] = 'image_id'
                res['person_uuid'] = 'person_uuid'
            # elif res.get('request_id') and res.get('masked_idcard')and res.get('image_id'):
            #     res['request_id'] = 'request_id'
            #     res['masked_idcard'] = 'masked_idcard'
            #     res['image_id'] = 'image_id'
            # elif res.get('request_id') and res.get('masked_idcard'):
            #     res['request_id'] = 'request_id'
            #     res['masked_idcard'] = 'masked_idcard'

            elif res.get('request_id') and res.get('image_one') and res.get('image_two'):
                res['request_id'] = 'request_id'
                res['image_one']['image_one_id'] = 'image_one_id'
                res['image_two']['image_two_id'] = 'image_two_id'
            elif res.get('request_id') and res.get('image_one'):
                res['request_id'] = 'request_id'
                res['image_one']['image_one_id'] = 'image_one_id'
            elif res.get('request_id') and res.get('image_two'):
                res['request_id'] = 'request_id'
                res['image_two']['image_two_id'] = 'image_two_id'
            elif res.get('request_id') and res.get('image_id') and res.get('liveness_data_id'):
                res['request_id'] = 'request_id'
                res['image_id'] = 'image_id'
                res['liveness_data_id'] = 'liveness_data_id'
            elif res.get('request_id') and res.get('image_id') and res.get('time_used'):
                res['request_id'] = 'request_id'
                res['time_used'] = 'time_used'
                res['image_id'] = 'image_id'
            elif res.get('request_id') and res.get('image_id'):
                res['request_id'] = 'request_id'
                res['image_id'] = 'image_id'
            elif res.get('request_id') and res.get('liveness_data_id'):
                res['request_id'] = 'request_id'
                res['liveness_data_id'] = 'liveness_data_id'
            elif res.get('request_id') and res.get('selfie_image_id'):
                res['request_id'] = 'request_id'
                res['selfie_image_id'] = 'selfie_image_id'
            elif res.get('request_id') and res.get('selfie') and res.get('historical_selfie'):
                res['request_id'] = 'request_id'
                res['selfie']['image_id'] = 'image_id'
                res['historical_selfie']['image_id'] = 'image_id'
            elif res.get('request_id') and res.get('historical_selfie'):
                res['request_id'] = 'request_id'
                res['historical_selfie']['image_id'] = 'image_id'
            elif res.get('request_id') and res.get('feature_image_id'):
                res['request_id'] = 'request_id'
                res['feature_image_id'] = 'feature_image_id'
            elif res.get("request_id") and res.get("selfie") and res.get("watermark_picture"):
                if res.get("selfie").get("image_id") and res.get("watermark_picture").get("image_id"):
                    res['request_id'] = 'request_id'
                    res["selfie"]['image_id'] = 'image_id'
                    res["watermark_picture"]["image_id"] = 'image_id'
            elif res.get("request_id") and res.get("selfie"):
                if res.get("selfie").get("image_id"):
                    res['request_id'] = 'request_id'
                    res["selfie"]['image_id'] = 'image_id'
            else:
                res['request_id'] = 'request_id'
            if res.get('hack_score') and res.get('verify_score'):
                res['hack_score'] = self.round_float(res.get('hack_score'), 3)
                res['verify_score'] = self.round_float(res.get('verify_score'), 3)
            elif res.get('hack_score'):
                res['hack_score'] = self.round_float(res.get('hack_score'), 3)
            elif res.get('verify_score'):
                res['verify_score'] = self.round_float(res.get('verify_score'), 3)
            elif res.get('confidences') and res.get('max_confidence'):
                res['max_confidence'] = self.round_float(res.get('max_confidence'), 3)
                for scores in res.get('confidences'):
                    for i in range(0, len(scores)):
                        scores[i] = self.round_float(scores[i], 3)
            elif res.get("confidence"):
                res['confidence'] = self.round_float(res.get('confidence'), 3)
            elif res.get("score"):
                res['score'] = self.round_float(res.get('score'), 3)

            self.assertDictEqual(res, path, '返回json不匹配:\n实际结果:[{first}]\n预期结果:[{second}]'.format(first=res, second=path))
            print('检查点成功。')
            print('实际结果：{first}'.format(first=res))
            print('预期结果：{second}'.format(second=path))

    # 获取测试用例中需要向后传递的value
    def transmit(self, name, path):
        node = self.json_value(path)
        if node:
            Client.VALUES[name] = node
        else:
            raise Exception('未获取到要传递的值:' + path)

    # 获取参数
    def value(self, name):
        v = Client.VALUES.get(name)
        if v:
            return v
        else:
            raise Exception('要获取的变量不存在:' + name)

    def db_values(self, sql):
        if DATABASE.HOST and DATABASE.USER and DATABASE.PASSWORD and DATABASE.NAME:
            db = None
            try:
                db = pymysql.connect(host=DATABASE.HOST, user=DATABASE.USER, password=DATABASE.PASSWORD, db=DATABASE.NAME)
                cursor = db.cursor()
                cursor.execute(sql)
                db.commit()
                return cursor.fetchall()
            except Exception as e:
                print(e)
                raise Exception('数据库操作失败')
            finally:
                if db:
                    db.close()
        else:
            raise Exception('数据库链接参数错误')

    def check_db1(self, exp, sql):
        data = self.db_values(sql)
        if data:
            self.check_equal(exp, data[0][0])
        else:
            self.assertFalse(True, '数据库取值无效：' + sql)

    def check_db2(self, path, sql):
        data = self.db_values(sql)
        exp = self.json_value(path)
        if data:
            if exp:
                self.check_equal(exp, str(data[0][0]))
            else:
                self.assertFalse(True, 'json取值无效：' + path)
        else:
            self.assertFalse(True, '数据库取值无效：' + sql)

    def write_headers(self, path):
        headers = ['status', 'url', 'apiid', 'file', 'data', 'response']
        try:
            with open(path, mode='a', encoding='utf-8', errors='ignore') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow(headers)
        except Exception as e:
            print(e)
            raise Exception('存储路径不存在')

    def write_to_csv(self, path):
        """向csv文件中写入数据"""
        try:
            with open(path, mode='a', encoding='utf-8', errors='ignore') as f:
                csv_write = csv.writer(f)
                csv_write.writerow([self.status_code, self.__url, self.__data.get('api_id'), self.__file,
                                    self.__data, self.res_to_json()])
        except Exception as e:
            print(e)
            raise Exception('路径不存在')

    def data_statistics(self, path):
        df = pandas.read_csv(path)
        return df[df.apiid == '557c656d71f54a7e8f8c681d7a9ab006'].status.value_counts()

    def write_bytes_to_csv(self, path):
        try:
            with open(path, mode='a', encoding='utf-8', errors='ignore') as f:
                csv_write = csv.writer(f)
                csv_write.writerow([self.status_code, self.__url, self.__data.get('api_id'), self.__file,
                                    self.__data, self.text.encode('utf-8')])
        except Exception as e:
            print(e)
            raise Exception('路径不存在')

    # 截取n位小数，不四舍五入
    def round_float(self, num, n):
        if isinstance(num, float):
            a, b = str(num).split('.')
            b = b[:n]
            return float('.'.join([a, b]))
        elif isinstance(num, str):
            try:
                a, b = num.split('.')
                b = b[:n]
                return '.'.join([a, b])
            except Exception:
                print("num字符串内容不是小数")
        elif num == 0 or num == '0':
            return num
        else:
            print("num参数不是小数")
