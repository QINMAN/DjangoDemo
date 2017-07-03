# coding:utf-8

class pro_1:
    count = '1'   # 类变量
    name_list = []
    def __init__(self, c):
        self.instance_count = c  #实例变量


print pro_1('3').count ,id(pro_1('3').count)
print pro_1.count, id(pro_1.count)

print '######## change by class #########'
pro_1.count = '66'
print pro_1('3').count, id(pro_1('3').count)
print pro_1.count, id(pro_1.count)


print '######## change by class instance #########'
p3 = pro_1('9')
p3.count = '3'
print p3.count, id(p3.count)
print pro_1.count, id(pro_1.count)


# nnnn
print pro_1('3').name_list ,id(pro_1('3').name_list)
print pro_1.name_list, id(pro_1.name_list)

print '######## change by class #########'
pro_1.name_list = ['a','b']
print pro_1('3').name_list, id(pro_1('3').name_list)
print pro_1.name_list, id(pro_1.name_list)


print '######## change by class instance #########'
p3 = pro_1('9')
p3.name_list = ['1','2']
print p3.name_list, id(p3.name_list)
print pro_1.name_list, id(pro_1.name_list)
print pro_1(4).name_list, id(pro_1(4).name_list)