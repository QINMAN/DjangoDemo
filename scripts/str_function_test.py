#coding:utf-8
a=" xxx yyy zzz "
print a.islower()
print a.isupper()
print a.upper()
print  a.lower()
print a.strip()
print a.lstrip()
print  a.rstrip()
print a.replace("xxx","ttt")
print a.split(" ")

a=[(1,2),(4,1),(5,3)]
a.sort(key=lambda x:x[1])
print a