#   @author: 马朝威 1570858572@qq.com
#   @time: 2019/1/6 22:49
from django.urls import path
from MyApp import views

urlpatterns = [
    path('index/', views.index),
    path('detail/<int:num>', views.detail)
]










