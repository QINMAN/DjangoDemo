#coding:utf-8
import time

def deca(func):
    def wrapper_func(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print end_time-start_time
        return result
    return wrapper_func

def deca_1(func):
    return lambda *args,**kwargs:None

@deca
def foo(a):
    time.sleep(3)
    return   a

#foo=deca(foo)
c=foo('abc')
d=foo("ab")
print  c

# class  Test(object):
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b