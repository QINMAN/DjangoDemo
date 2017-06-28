# coding:utf-8

# with open('seq.txt','r') as f:
#     print f.read()

import sys

class test1():

    def __enter__(self):
        print 'enter'
        return

    def __exit__(self, exc_type, exc_val, exc_tb):

        print 'exit'
        print exc_type, exc_val, exc_tb
        return True # 返回 True 的话不抛出异常，返回 False 抛出异常


with test1() as t:
    print 'test'

    raise NameError('name')
    sys.exit()
    print 'never here'


