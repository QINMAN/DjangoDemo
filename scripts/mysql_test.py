#coding:utf-8

import MySQLdb
print "###### write  to mysql ######"
conn=MySQLdb.connect(host="113.10.195.169",port=3306,user="mm",passwd="mm_123456",
                     db="mm_test")
cursor=conn.cursor()
cursor.execute("insert ignore into category(catename) VALUES(%s)",("test",))
cursor.close()
conn.commit()
conn.close()

print "###### read  from mysql #####"
conn=MySQLdb.connect(host="113.10.195.169",port=3306,user="mm",passwd="mm_123456",
                     db="mm_test",charset="utf8")
cursor=conn.cursor()
cursor.execute("select cid  from category",())
result=cursor.fetchall()
cursor.close()
conn.close()
print result