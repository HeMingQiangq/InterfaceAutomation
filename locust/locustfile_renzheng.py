# coding=utf-8

from locust import HttpLocust, TaskSet, task
import os,sys
import requests
import json
pack_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(pack_dir, "locust_file/ocreidcard")
data = {"api_id": "557c656d71f54a7e8f8c681d7a9ab006",
            "api_secret": "7ff1e984d75b48f9b3ba3aa3033ad252"}

class WebsiteTasks(TaskSet):
    def on_start(self):
        # self.client.post("/login", {
        #     "api_id": "557c656d71f54a7e8f8c681d7a9ab006",
        #     "api_sercret": "7ff1e984d75b48f9b3ba3aa3033ad252"
        # })
        #
        print('初始化完成')


        
    @task()
    def selfie_idnumber_verification(self):
        '''
        人证比对，通过身份证号、姓名和自拍照去第三方进行身份验证功能
        '''
        file = {'selfie_file': open(data_dir + '/01_test.jpeg', 'rb+')}
        data['id_number'] = '*******'
        data['name'] = '何明强'
        res = self.client.post("/identity/selfie_idnumber_verification", data=data, files=file)
    @task
    def liveness_idnumber_verification(self):
        '''
        人证比对，通过身份证号、姓名和移动端活体检测SDK返回的protobuf文件中的活体数据去第三方进行身份验证功能
        '''
        data['id_number'] = '510181198110225316'
        data['name'] = '杨庆松'
        file = {'liveness_data_file':open(data_dir+'/protobuf.proto','rb+')}
        res = self.client.post("/identity/liveness_idnumber_verification",data=data,files=file)




class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    #host = "http://100.73.18.123:19641"
    min_wait = 0
    max_wait = 0