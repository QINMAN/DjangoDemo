# coding:utf-8

from django.http import HttpResponse
from django.template import Template, Context,RequestContext
import datetime
from django.shortcuts import render_to_response
import models
import time

def hello(request):
    return HttpResponse("HELLO")

def temp(request):
    d = datetime.datetime.now()
    # 格式化
    # d.strftime("%Y%m%d %H:%M:%S")

    return render_to_response("template.html",
                              {"person_name":"QINMAN","company":"BAIDU","ship_date":d,"passed":True,"list":[1,2,3]},
                              context_instance=RequestContext(request))


def studentList(request):
    s_list_all = models.student.objects.all()
    s_list_filter=models.student.objects.filter(age__in=[16,18])

    return render_to_response("stu.html",{"s_list":s_list_all},context_instance = RequestContext(request))
