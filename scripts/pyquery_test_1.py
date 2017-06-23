#coding:utf-8
import pyquery
html_str="<div><a></a><div><a href='www.baidu.com'>xxxxx<img src='/static/xx'></a></div></div>"

doc = pyquery.PyQuery(html_str)

div_ele = doc('div')[1]

div_doc = pyquery.PyQuery(div_ele)

result = div_doc('a')

print result,type(result)

print result.text()

print result.html()
