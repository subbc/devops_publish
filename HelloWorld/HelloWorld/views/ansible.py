#!/usr/bin/env python  
# _#_ coding:utf-8 _*_ 
import uuid,os,json
from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import cgi,cgitb

def index(request):
#    return HttpResponse("发布成功！！！")
    mes_type = request.POST.get('stra_1')
    mes_web = request.POST.get('stra_2')
    mes_yn = request.POST.get('stra_3')
    print(mes_type,mes_web,mes_yn)
    if mes_yn == 'no':
        return HttpResponse("发布失败！！！")
    else:
        if mes_web == 'xfalse':
            return HttpResponse("发布无效，请选择站点！！！")
        else:
            print("开始执行shell脚本")
            if mes_type == 'git':
                os.system("/opt/script/git_update.sh %s" % (mes_web))  ###执行shell脚本
            else:
                os.system("/opt/script/composer_update.sh %s" % (mes_web))  ###执行shell脚本
            print('shell脚本执行完成')
            return HttpResponse("发布成功！！！")

def publish(request):
    context = {}
    context['dj'] = '运维发布平台页面'
    context['submit'] = '准备发布中……'
    return render(request,"publish.html",context)

#form = cgi.FieldStorage()
#str_a = form.getvalue('stra_1')
#print("<h2>stra_1:%s</h2>" % (str_a))
#name = str_a
#if name == 'yes':
#    print("发布成功！！！")
#else:
#    print("发布失败！！！")




