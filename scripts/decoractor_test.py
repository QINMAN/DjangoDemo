#coding:utf-8
import datetime

def deca(func):
    def test_func(*args, **kwargs):
        print datetime.datetime.now()
        result = func(*args, **kwargs)
        print datetime.datetime.now()
        return result
    return test_func

@deca
def foo(a):
    print  a
    pass

foo(123)

print  "#############"
def speed_decoractor(fun):
    def real_fun(*args,**kwargs):
        print datetime.datetime.now()
        result=fun(*args,**kwargs)
        print datetime.datetime.now()
        return result
    return real_fun

@speed_decoractor
def foo(x,y):
    print "this  a  foo fun"
    return x+y
#foo=speed_decoractor(foo)

c= foo(1,2)
