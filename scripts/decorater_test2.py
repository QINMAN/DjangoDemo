# coding:utf-8

# 得到用装饰器的函数的函数名和参数的值

import functools
import inspect

def is_admin(func):
    @functools.wraps(func) # 正确的获取被装饰函数的属性
    def wrapper(*args, **kwargs):
        func_args = inspect.getcallargs(func, *args, **kwargs)
        if func_args.get('username') != 'admin':
            # if kwargs.get('username') != 'admin':
                print 'This is not admin'
        return func(*args, **kwargs)
    return wrapper

@is_admin
def foo(username, food = 'cho'):
    print 'username = {0}, {1}'.format(username, food)
    print 'foo' + ' ' + str(username)


foo('admin')
print foo.__name__


