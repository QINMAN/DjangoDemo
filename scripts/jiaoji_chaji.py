#coding:utf-8

list_1 = ['a','b','c','c','d','d']

list_2 = ['b','d']

cha_list = []

jiao_list = []

for i in list_1:
    if i not in list_2:
        if i not in cha_list:
            cha_list.append(i)
    else:
        if  i not in jiao_list:
            jiao_list.append(i)

print cha_list,jiao_list