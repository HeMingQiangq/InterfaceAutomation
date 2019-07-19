import unittest
import HTMLTestReportCN
import time
import shutil
import sys
from util import *
import re
import os,sys
from client import *
data= os.system('python./LivenessHackDetect1.py')
os.system('python./LivenessSelfieVerification.py')

def get_value(dic, name):
    source = dic.get(name)
    if source is None or source == '':
        return None
    else:
        variable_regexp = r"\$([\w_]+)"
        result = re.findall(variable_regexp, source)
        if len(result) > 0:
            value = DATA.get(result[0])
            if value:
                source = source.replace('$'+result[0], value)
            else:
                return None
        return source


if __name__ == '__main__':


    suite = unittest.defaultTestLoader.discover(start_dir=base_dir + '/interface', pattern='VerifyIdNameBankcard_JDSK.py')

    #suite = unittest.defaultTestLoader.discover(start_dir=base_dir + '/interface', pattern='DbInfo.py')
    # suite = unittest.TestSuite()
    # cases = util.read_runconfig(base_dir + '/config.xml', 'cases')c
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # for case in cases:
    #     p_name = case.split('-')[0]
    #     c_name = case.split('-')[1]
    #     # p = importlib.import_module(package='cases.' + p_name, name=p_name)
    #     FUNC_TEMPLATE1 = 'from interface.{package} import {classes}'
    #     FUNC_TEMPLATE2 = 'suite.addTest({case}("test_{method}"))'
    #     exec(FUNC_TEMPLATE1.format(package=p_name, classes=p_name))
    #     exec(FUNC_TEMPLATE2.format(case=p_name, method=c_name))

    title = '%s.html' % now
    fp = open(os.path.join(base_dir, 'report', title), 'wb')
    HTMLTestReportCN.HTMLTestRunner(stream=fp, title='接口测试报告').run(suite)
    fp.close()
    # shutil.copyfile(sys.argv[0] + '\\..\\report\\' + title, sys.argv[0] + '\\..\\report\\report.html')
    # excel加载用例模式下
    # now = time.strftime("%Y-%m-%d %H_%M_%S")
    # result_path = base_dir + '/result/' + now + '_result.csv'
    # case_path = base_dir + '/excel_cases/%s.xlsx' % read_runconfig(base_dir+'/config.xml', 'excelcases')[0]
    # cases = util.read_config_excel(case_path, '用例').get('用例')
    # if cases:
    #     suite = unittest.TestSuite()
    #     for case in cases:
    #         id = get_value(case, '用例编号')
    #         des = get_value(case, '用例描述')
    #         url = get_value(case, '地址')
    #         method = get_value(case, '方法类型')
    #         type = get_value(case, '参数类型')
    #         headers = get_value(case, '请求头')
    #         files = get_value(case, '文件参数')
    #         data = get_value(case, '参数')
    #         checks = get_value(case, '检查点')
    #         if not headers:
    #             headers = {}
    #         if not files:
    #             files = {}
    #         if not data:
    #             data = {}
    #         if checks:
    #             checks = checks.split('&')
    #         FUNC_TEMPLATE = """class {classes}(unittest.TestCase):
    # def test_{id}(self):
    #     '''{des}'''
    #     url = '{url}'
    #     method = Method.{method}
    #     type = Type.{type}
    #     headers = {headers}
    #     files = {files}
    #     data = {data}
    #     path = '{path}'
    #     client = Client(url=url, method=method, type=type)
    #     client.set_headers(headers)
    #     client.set_files(files)
    #     client.set_data(data)
    #     client.send()
    #     client.write_to_csv(path)\n"""
    #         func = FUNC_TEMPLATE.format(classes=id.upper(), id=id, des=des, url=url, method=method, type=type,
    #                                     headers=headers, files=files, data=data, path=result_path)
    #         for check in checks:
    #             func += '        client.%s\n' % check
    #         exec(func)
    #         ADD = 'suite.addTest({case}("test_{method}"))'
    #         exec(ADD.format(case=id.upper(), method=id))
    #     title = '%s.html' % now
    #     fp = open(os.path.join(base_dir, 'report', title), 'wb')
    #     HTMLTestReportCN.HTMLTestRunner(stream=fp, title='接口测试报告').run(suite)
    #     fp.close()
    # shutil.copyfile(sys.argv[0] + '\\..\\report\\' + title, sys.argv[0] + '\\..\\report\\report.html')


