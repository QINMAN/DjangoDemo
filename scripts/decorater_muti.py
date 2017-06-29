# coding:utf-8
# 多个装饰器

def make_bold(func):
    def wrapper(*args, **kwargs):
        return '<b>' + func() + '</br>'
    return wrapper

def make_italic(func):
    def wrapper(*args, **kwargs):
        return '<i>' + func() + '</i>'
    return wrapper


@make_bold
@make_italic
def foo():
    return 'hello' # foo 函数返回一个字符串，才能使用装饰器


print foo()