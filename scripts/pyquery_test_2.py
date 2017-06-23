#coding:utf-8
import pyquery
import urllib2

url = 'http://news.baidu.com/'
html_str = urllib2.urlopen(url).read().decode('utf-8')

html_doc = pyquery.PyQuery(html_str)

result = html_doc('.hdline0 a').text()
# class_ele=class_doc[0]
#
# strong_doc = pyquery.PyQuery(class_ele)('strong')
# content_ele = strong_doc('a')[0]
#
# content_doc = pyquery.PyQuery(content_ele)
#
# result = content_doc.text()

print result

