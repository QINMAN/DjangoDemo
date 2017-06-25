#coding:utf-8
import time

class TestMideleware(object):

    def process_request(self,request):
        request.ip="8.8.8.8"

    def process_response(self,request,response):
        response.set_cookie("test",str(time.time()),max_age=500)
        return response
