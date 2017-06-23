#coding:utf-8
import pyquery
html_str="<div><a>test</a><input></input><a href='xxx'>test</a></div>"
doc=pyquery.PyQuery(html_str)
# print type(doc),doc,len(doc)
result= doc("a")
# print type(result),result,len(result)
for i in doc.children():
    print i
    i_doc=pyquery.PyQuery(i)
    print type(i_doc)
