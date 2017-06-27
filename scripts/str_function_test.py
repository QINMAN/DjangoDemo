#coding:utf-8
a=" xxx yyy zzz "
print a.islower() # 判断是否是小写
print a.isupper() # 判断是否是大写
print a.upper() # 转为大写
print  a.lower()  # 转为小写
print a.strip() # 去掉两边的缩进
print a.lstrip() # 去掉左边的缩进
print  a.rstrip() # 去掉右边的缩进
print a.replace("xxx","ttt") # 替换某部分字符串
print a.split(" ") # 通过给定的字符串分字符串

a=[(1,2),(4,1),(5,3)]
a.sort(key=lambda x:x[1])
print a