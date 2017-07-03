#coding:utf-8

import copy
a = [1, 2, 3, 4, ['a', 'b']]  #原始对象

b = a  #赋值，传对象的引用
c = copy.copy(a)  #对象拷贝，浅拷贝
# c=[a[0],a[1],a[2],a[3],a[4]]
d = copy.deepcopy(a)  #对象拷贝，深拷贝

a.append(5)  #修改对象a
a[4].append('c')  #修改对象a中的['a', 'b']数组对象

print 'a = ', a, id(a), 'ip a[4]',id(a[4])
print 'b = ', b, id(b), 'ip a[4]',id(b[4])
print 'c = ', c, id(c), 'ip a[4]',id(c[4])
print 'd = ', d, id(d), 'ip a[4]',id(d[4])

# 输出结果：
# a =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
# b =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
# c =  [1, 2, 3, 4, ['a', 'b', 'c']]
# d =  [1, 2, 3, 4, ['a', 'b']]