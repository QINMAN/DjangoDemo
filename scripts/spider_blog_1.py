#coding:utf-8

import urllib2
import pyquery
import MySQLdb
from sqlConn import SqlConn

def readCate():
    conn = MySQLdb.connect(host="113.10.195.169", port=3306, user='mm',
                           passwd='mm_123456', db='mm_test', charset='utf8')
    cursor = conn.cursor()
    # SqlConn().execute('insert into category (catename) VALUES (%s) ,(context, )')
    sql = 'select * from category'
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data


def saveCate(context):

    conn = MySQLdb.connect(host="113.10.195.169",port=3306,user='mm',
                           passwd='mm_123456',db='mm_test',charset='utf8')
    cursor = conn.cursor()

    # sql = 'insert into category (catename) VALUES (%s)' % context
    # SqlConn().execute(sql)

    cursor.execute('insert into category (catename) VALUES (%s)',(context,))
    conn.commit()
    cursor.close()
    conn.close()
    print readCate()


def update(value, cid):
    conn = MySQLdb.connect(host="113.10.195.169", port=3306, user='mm',
                           passwd='mm_123456', db='mm_test', charset='utf8')
    cursor = conn.cursor()
    # SqlConn().execute('insert into category (catename) VALUES (%s) ,(context, )')
    cursor.execute('update category set catename = %s WHERE cid = %s', (value, cid))
    conn.commit()
    cursor.close()
    conn.close()
    print readCate()


def delete(context):
    conn = MySQLdb.connect(host="113.10.195.169", port=3306, user='mm',
                           passwd='mm_123456', db='mm_test', charset='utf8')
    cursor = conn.cursor()
    # SqlConn().execute('insert into category (catename) VALUES (%s) ,(context, )')
    cursor.execute('delete from category WHERE catename =  %s' , (context,))
    conn.commit()
    cursor.close()
    conn.close()
    print readCate()


url = 'http://www.yangqq.com/jstt/'
response = urllib2.urlopen(url)
result = response.read().decode('gbk')
doc = pyquery.PyQuery(result)

# read
# print readCate()

# update
update('test33',33)

# delete
# delete('test')

# save
# for ele in doc(".rnavs a"):
#     ele_doc = pyquery.PyQuery(ele)
#     content=ele_doc.text()
#     saveCate(content)
