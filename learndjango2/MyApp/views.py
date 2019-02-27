from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('samma is good man !!!')


def detail(request, num):
    return HttpResponse('detail-%d'%num)