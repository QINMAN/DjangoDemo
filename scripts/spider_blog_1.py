#coding:utf-8

import urllib2
import pyquery
import MySQLdb


def saveCate(context):
    conn = MySQLdb.connect(host="113.10.195.169",port=3306,user='mm',
                           passwd='mm_123456',db='mm_test',charset='utf8')
    cursor = conn.cursor()
    cursor.execute('insert into category (catename) VALUES (%s)',(context,))
    conn.commit()
    cursor.close()
    conn.close()

url = 'http://www.yangqq.com/jstt/'
response = urllib2.urlopen(url)
result = response.read().decode('gbk')
doc = pyquery.PyQuery(result)

for ele in doc(".rnavs a"):
    ele_doc = pyquery.PyQuery(ele)
    content=ele_doc.text()
    saveCate(content)
    print content
