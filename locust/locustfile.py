# coding=utf-8

from locust import HttpLocust, TaskSet, task
import os,sys
import requests
import json
pack_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(pack_dir, "locust_file/ocreidcard")
data = {"api_id": "",
            "api_secret": ""}

class WebsiteTasks(TaskSet):
    def on_start(self):
        # self.client.post("/login", {
        #     "api_id": "557c656d71f54a7e8f8c681d7a9ab006",
        #     "api_sercret": "7ff1e984d75b48f9b3ba3aa3033ad252"
        # })
        #
        print('初始化完成')

    @task(41)
    def ocridcard(self):
        '''idcard'''
        file = {'file': open(data_dir + "/正常人像照.jpg" ,'rb')}
        rus_data = json.dumps(data)
        self.client.post('/ocr/idcard', data = data ,files=file)
        

    @task(1)
    def ocrbankcard(self):
        '''ocrbankcard'''
        file = {'file': open(data_dir + "/工商.jpg", 'rb')}
        self.client.post('/ocr/bankcard', data=data, files=file)

    @task()
    def ocrparse_idcard_ocr_result(self):
        '''正常身份证正面'''
        file = {'file':open(data_dir + '/frontfile','rb')}
        self.client.post('/ocr/parse_idcard_ocr_result',data = data,files=file)

    @task()
    def ocrparse_bankcard_ocr_result(self):
        '''正常银行卡'''
        file = {'file':open(data_dir + '/交通','rb')}
        self.client.post('/ocr/parse_bankcard_ocr_result',data = data ,files = file)

    @task(2)
    def dataverify_id_name(self):
        '''二要素'''
        datas = data.copy()
        datas['id_number']= '360430198104050327'
        datas['name'] = '祝芳'
        # data={"api_id": "557c656d71f54a7e8f8c681d7a9ab006",
        #      "api_secret": "7ff1e984d75b48f9b3ba3aa3033ad252",
        # "name": "惠强",
        # 'id_number': '372922198710065431'}
        
        self.client.post('/data/verify_id_name',data=datas)

    @task()
    def dataverify_id_name_bankcard_phone(self):
        '''四要素'''
        datas = data.copy()
        datas['name'] = '张坚'
        datas['id_number'] = '441230197602070473'
        datas['card_number'] = '6013827013003249183'
        datas['phone_number'] = '13560944266'
        result=self.client.post('/data/verify_id_name_bankcard_phone',data = datas)

    # @task()
    # def liveness_image(self):
    #     '''活体检测'''
    #     datas =data.copy()
    #     datas['motions']='BLINK MOUTH'
    #     datas['complexity']= 1
    #     file = {'liveness_data_file':open(data_dir + '/眨眼张嘴.mp4','rb')}
    #     self.client.post('/liveness/check_liveness',data=datas,files=file)
    #     client.transmit('image_id', '$.image_id')

    @task()
    def iveness_image(self):
        datas = data.copy()
        datas['image_id'] = 'cf8e45503c144a138059490dc71d4ca1'
        self.client.get('/liveness/liveness_image/cf8e45503c144a138059490dc71d4ca1',params=datas)
        
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
    @task
    def handhold_idcard_verification(self):
        '''
        人脸比对，将手持身份证照中的被拍人的脸和手持身份证上的人脸进行比对
        '''
        file = {'file':open(data_dir+'/handhold.jpg','rb+')}
        res = self.client.post("/identity/handhold_idcard_verification",data=data,files=file)
    @task
    def selfie_watermark_verification(self):
        '''
        人脸对比，将人脸照片与后台带水印照片进行比对
        '''
        file = {
            'selfie_file':open(data_dir+'/feishuiying.jpg','rb+'),
            'watermark_picture_file':(open(data_dir+'/shuiying.jpg','rb+'))
        }
        res = self.client.post("/identity/selfie_watermark_verification",data=data,files=file)

    @task
    def historical_selfie_verification(self):
        '''
        人脸对比，将两张人脸图片进行比对
        '''
        file = {
            'selfie_file':open(data_dir+'/historical.jpg','rb+'),
            'historical_selfie_file':open(data_dir+'/copyhistorical.jpg','rb+')
        }
        res = self.client.post("/identity/historical_selfie_verification",data=data,files=file)

    @task
    def selfie_hack_detect(self):
        '''
        防hack,验证用户自拍照是否活体
        '''
        file = {'file':open(data_dir+'/selfilehack.jpg','rb+')}
        res = self.client.post("/hackness/selfie_hack_detect",data=data,files=file)

    @task
    def liveness_hack_detect(self):
        '''
        防检测用户拍摄的活体数据是否活人
        '''
        file = {'liveness_data_file': open(data_dir + '/protobuf.proto', 'rb+')}
        res = self.client.post("/hackness/liveness_hack_detect", data=data, files=file)



class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    #host = "http://100.73.18.123:19641"
    min_wait = 0
    max_wait = 0