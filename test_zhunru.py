# --**coding:utf-8**--
import requests,json


def test():
    url = "https://zropenapi.jd.com/api/zr-bankcard4-jk"
    data = {'appkey': '9c75368268e54b17b0f62184499d87a1',
            'cust_id': 350623197206013034,
            'name': '杨志金',
            'bank_card_num': 6217933800493783,
            'mobile': 18859201867,
            'source_list': 1
            }
    res = requests.post(url=url,data=json.dumps(data))
    for i in res:
        print (i)
    pass

if __name__ == '__main__':
    test()