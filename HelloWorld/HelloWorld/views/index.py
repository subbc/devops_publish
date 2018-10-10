#!/usr/bin/env python  
# _#_ coding:utf-8 _*_  
import random,os
from django.http import HttpResponseRedirect,JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

#@login_required(login_url='/login')
def index(request):
    #    return HttpResponse("打开网页的第一个页面，good！！！ ")
    context = {}
    context['hello'] = 'Hello world!!!'
    return render(request,'index.html',context)
