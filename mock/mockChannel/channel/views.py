# --**coding:utf-8**--
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
import returnInfo
# Create your views here.

def index(request):
    # test
    return HttpResponse('test')

def nanjingZS(request):
    '''
    :param request: 当前get，未对入参做校验
    :return:南京甄视写死json串
    '''
    returnMessage = returnInfo.nanjingZs()
    return JsonResponse(returnMessage)

def bankCard(request):
    '''
    :param request: 当前get，未对入参做校验
    :return: ocr/bankcard  改成了json串
    '''
    bankCardInfo = returnInfo.OCRBankCard()
    return JsonResponse(bankCardInfo)

def jiupaiFourElements(request):
    '''
    :param request: 当前get，未对入参做校验
    :return: 九派四要素，直接return字符串
    '''
    return HttpResponse(returnInfo.jiupaiFourElements)
    pass
def jiupaiTwoElements(request):
    '''
    :param request: 当前get，未对入参做校验
    :return: 九派二要素，直接return字符串
    '''
    return HttpResponse(returnInfo.jiupaiTwoElements)
