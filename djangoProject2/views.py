# -*- codeing = utf-8 -*-
# @Time : 2021-05-29 23:50
# @Author : WangJun
# @File : views.py
# @Software : PyCharm

from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world!你好")

def runoob(request):
    #views_name = "菜鸟教程"
    views_list = ["菜鸟教程1", "菜鸟教程2", "菜鸟教程3","菜鸟教程5",,"菜鸟教程6"]
    return render(request, "runoob.html", {"hello": views_list})
    #context          = {}
    #context['hello'] = 'Hello World!'
    #return render(request, 'runoob.html', context)