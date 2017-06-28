# coding:utf-8

import MySQLdb
import random

class SqlConn():
    version = 1.0
    def __init__(self):
        self.conn = MySQLdb.connect(host="113.10.195.169",port=3306,user='mm',
                           passwd='mm_123456',db='mm_test',charset='utf8')
        self.cursor = self.conn.cursor()


    def commit(self):
        self.conn.commit()
        #self.cursor.close()
        #self.conn.close()

    # insert data
    def insert_data(self, table, params_dic):
        if(isinstance(params_dic, dict)) :
            col_names = ''
            # values = ''

            items = params_dic.items()
            param_keys = [i[0] for i in items]
            params_value = [i[1] for  i in items]

            col_names = ','.join(param_keys)
            #values = ','.join(params_value)
            # for key in params_dic:
            #     col_names += key + ', '
            #     values += params_dic[key] + ', '

            # print col_names
            # values = 'test_context , test_title'
            # self.cursor.execute('insert into %s (%s) VALUES (%s)', (table,col_names, values))
            # print  'insert into %s (%s) VALUES (%s)'% (table,col_names,",".join(["%s"*len(params_value)]))
            self.cursor.execute('insert into %s (%s) VALUES (%s)'% (table,col_names,",".join(["%s"]*len(params_value))), params_value)
            # self.cursor.execute("insert into xx(a,b) VALUES(%s,%s)",xxxxs)
            self.commit()

    # delete data
    def delete_data(self, table, params_dic):
        if(params_dic and len(params_dic) > 0):
            _=params_dic.items()
            params_keys=[i[0] for i in _]
            params_values=[i[1] for i in _]
            predicate = " and ".join([i+"=%s " for i in params_keys])
            self.cursor.execute('delete from %s WHERE %s' % (table, predicate), params_values)

        else:
            self.cursor.execute('delete from %s'%table)
        self.commit()


    def update_data(self, table, update_dic,where_dic={}):
        if len(where_dic)>0:
            _ = update_dic.items()
            update_keys = [i[0] for i in _]
            update_values = [i[1] for i in _]
            _=where_dic.items()
            where_keys=[i[0]  for i in _]
            where_values=[i[1] for i in _]
            update_str=",".join([i+"=%s" for i in update_keys])
            where_str = " and ".join([i + "=%s " for i in where_keys])
            self.cursor.execute('update %s set %s WHERE %s ' % (table, update_str,where_str),
                                update_values+where_values)
        else:
            _ = update_dic.items()
            update_keys = [i[0] for i in _]
            update_values = [i[1] for i in _]

            update_str = ",".join([i + "=%s" for i in update_keys])
            self.cursor.execute('update %s set %s ' % (table, update_str),
                                update_values)

        self.commit()


    def select_data(self,table,where_dic={}):
        cursor=self.conn.cursor()
        if len(where_dic)>0:
            items = where_dic.items()
            column_names = [i[0] for i in items]
            values = [i[1] for i in items]
            _ = ' and '.join([i + '=%s' for i in column_names])
            self.cursor.execute('select * from %s where %s'%(table,_),values)
        else:
            self.cursor.execute('select * from %s'%(table,))
        result= self.cursor.fetchall()
        cursor.close()
        return result

    @staticmethod
    def testStataicMe():
        pass

    @classmethod
    def testClaaa(cls):

        pass

conn=SqlConn()
# conn.delete_data("category",{"cid":35})

# result= conn.select_data("article")
# for i in result:
#     cid=random.sample([36,37,39,40],1)[0]
#     print i[0],cid
#     conn.update_data("article",{"cid":cid},{"aid":int(i[0])})
#self.cursor.execute('delete from category WHERE cid=%s', (35,)
#   delete from category  where  cid=%s