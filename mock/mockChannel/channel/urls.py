# Create by author: hemq

from django.conf.urls import url
from . import views

app_name = 'channel'

urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^nanjing/$',views.nanjingZS,name='nanjingZS'),
    url(r'^bankcard/$',views.bankCard,name='bankCard'),
    url(r'^jiupaifour/$',views.jiupaiFourElements,name='jiupaiFourElements'),
    url(r'^jiupaitwo/$',views.jiupaiTwoElements,name='jiupaiTwoElements'),

]
