#coding:utf-8

import sqlConn

conn = sqlConn.SqlConn()



import re
s = '1234567893333333'
res_1 = re.search(r'\d+?',s).group()
res_2 = re.search(r'\d+',s).group()
print res_1
print res_2
