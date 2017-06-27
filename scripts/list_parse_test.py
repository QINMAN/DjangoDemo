#coding:utf-8
a=range(1,10)
b=[ i for i in a if i>2 and i<5  ]
print b

try:
    pass
except Exception,e:
    pass
else:
    pass
finally:
    pass

a = ['This', 'is','a','good','job']

a.sort(key=lambda x:x.lower()) # key 是一个函数，该函数对要排序的 list 进行处理，但是并不会改变 list 本身

print a
