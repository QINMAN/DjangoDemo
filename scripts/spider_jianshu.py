#coding:utf-8

import urllib2
import pyquery

url = 'http://www.jianshu.com/'
html_str = urllib2.urlopen(url).read().decode('utf-8')
result = pyquery.PyQuery(html_str)(".title")

href_list=[]
for i in result:
    _= 'http://www.jianshu.com' + pyquery.PyQuery(i).attr('href')
    href_list.append(_)

# print html_str
# print result
# print href_list

import MySQLdb
def write_data(title,content):
    conn = MySQLdb.connect(host="113.10.195.169",port=3306,user="mm",passwd="mm_123456",
                     db="mm_test",charset="utf8")
    cursor = conn.cursor()
    cursor.execute('insert into article (title, context) VALUES (%s,%s)',(title, content))
    conn.commit()
    cursor.close()
    conn.close()

for url in href_list:
    try:
        detail_str = urllib2.urlopen(url).read().decode('utf-8')
        doc = pyquery.PyQuery(detail_str)
        title = doc('.title').text()
        content = doc('.show-content').text()
        write_data(title,content)
    except Exception, e:
        pass


