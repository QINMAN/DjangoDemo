# coding:utf-8

import MySQLdb

class SqlConn():

    def __init__(self):
        self.conn = MySQLdb.connect(host="113.10.195.169",port=3306,user='mm',
                           passwd='mm_123456',db='mm_test',charset='utf8')
        self.cursor = self.conn.cursor()


    def commit(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def execute(self, sql):
        self.cursor.execute(sql)
        self.commit()

