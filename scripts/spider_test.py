#coding:utf-8
import urllib2
import pyquery

response=urllib2.urlopen("http://www.baidu.com/")
result=response.read().decode("utf-8")
print result
doc=pyquery.PyQuery(result)
for input in  doc("input"):
    print pyquery.PyQuery(input).attr("name")

