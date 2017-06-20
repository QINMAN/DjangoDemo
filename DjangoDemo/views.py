# coding:utf-8

from django.http import HttpResponse
from django.template import Template, Context
import datetime

import time

def hello(request):
    return HttpResponse("HELLO")

def temp(requst):
    d = datetime.datetime.now()
    # 格式化
    # d.strftime("%Y%m%d %H:%M:%S")
    t = Template("Hello:{{ name }}  {{ date.minute }}")

    c = Context({"name": "John", "date": d})
    result = t.render(c)
    return HttpResponse(result)



