from django.http import HttpResponse
from django.template import Template,Context
import time

def hello(request):
    return HttpResponse("HELOO")

def temp(requst):
    t = Template("Hello:{{ name }}")

    c = Context({"name":"John"})
    result = t.render(c)
    return HttpResponse(result)



