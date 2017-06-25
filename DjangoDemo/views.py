# coding:utf-8

from django.http import HttpResponse
from django.template import Template, Context,RequestContext
import datetime
from django.shortcuts import render_to_response
import models
import time

def hello(request):

    respense = HttpResponse()
    if request.COOKIES.has_key('test_1'):
        v = request.COOKIES['test_1']
        respense.set_cookie('test_1', int(v)+1)
    else:
        respense.set_cookie('test_1',1)

    # return HttpResponse(request.ip )
    # request.session["user"]="abc"
    # request.session["userid"]="123"

    print  request.session['user']
    return respense


def temp(request):
    d = datetime.datetime.now()
    # 格式化
    # d.strftime("%Y%m%d %H:%M:%S")
    print   request.ip

    return render_to_response("template.html",
                              {"person_name":"QINMAN","company":"BAIDU","ship_date":d,"passed":True,"list":[1,2,3]},
                              context_instance=RequestContext(request))


def studentList(request):
    s_list_all = models.student.objects.all()
    s_list_filter=models.student.objects.filter(age__in=[16,18])

    return render_to_response("stu.html",{"s_list":s_list_all},context_instance = RequestContext(request))
