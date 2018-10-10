#!/usr/bin/env python
# _#_ coding:utf-8 _*_

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render,HttpResponse
from django.conf.urls import url
import sys,os,getpass

def login(request):
    return render(request, 'login.html')

def baobao(request):
    #获取用户提交的数据，做是否登录成功的判断
    email = request.POST
    print(request.POST)
    return HttpResponse('O98OK')

def register(request):
    return True

def logout(request):
    auth.logout(request)
#    return HttpResponseRedirect('/login')
    return render(request, 'loginout.html',context)