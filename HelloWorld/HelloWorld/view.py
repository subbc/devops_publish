#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world ! ")

def hellox(request):
    context          = {}
    context['hello'] = 'Hello World!!!'
    return render(request, 'hello.html', context)

