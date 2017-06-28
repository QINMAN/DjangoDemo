#coding:utf-8

import urllib2
import pyquery
import MySQLdb
import sqlConn

href_list=[]
base_url = 'http://www.jianshu.com'

url_list = ['/c/avQwgf','/c/00bd0686bc41','/c/GQ5FAs','/c/vHz3Uc','/c/7b2be866f564',
            '/c/V2CqjW','/c/Jgq3Wc','/c/xYuZYD','/c/80e7d5d15e71','/c/dqfRwQ',
            '/c/8c92f845cd4d', '/c/5cc4460bb4a0']

for i in url_list:
    url = base_url + i
    html_str = urllib2.urlopen(url).read().decode('utf-8')
    result = pyquery.PyQuery(html_str)("a")(".title")

    for i in result:
        _ = base_url + pyquery.PyQuery(i).attr('href')
        href_list.append(_)

def write_data(title,content):
    conn = MySQLdb.connect(host="113.10.195.169",port=3306,user="mm",passwd="mm_123456",
                     db="mm_test",charset="utf8")
    cursor = conn.cursor()
    cursor.execute('insert into article (title, context) VALUES (%s,%s)',(title, content))
    conn.commit()
    cursor.close()
    conn.close()

db_handle = sqlConn.SqlConn()

db_handle.delete_data(table='article', params_dic={})
for url in href_list:
    try:
        detail_str = urllib2.urlopen(url).read().decode('utf-8')
        doc = pyquery.PyQuery(detail_str)
        title = doc('.title').text()
        context = doc('.show-content').text()
        # write_data(title,context)
        # db_handle = sqlConn.SqlConn()
        # db_handle.insert_data('article', {'title':title, 'context':context})

    except Exception, e:
        print e
        # pass


