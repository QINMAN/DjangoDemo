# coding:utf-8

import json

# dict = {'name':'秦曼', 'gender':'female'}
#
# # 序列化
# dump_res = json.dumps(dict, ensure_ascii=False)
# print dump_res, type(dump_res)
#
# # 序列化到文件
# dump_file_res = json.dump(dict, open('seq.txt','w'), ensure_ascii=False)
# print dump_file_res, type(dump_file_res)
#
# # 反序列化
# load_res = json.loads(dump_res)
# print load_res, type(load_res)

# 对文件中的数据反序列化
# load_file_res = json.load(open('seq.txt','r'))
# print load_file_res, type(load_file_res)
# load_file_res=dict([(i,j.encode("utf-8"))  for i,j in load_file_res.items()])
# print load_file_res
# for i,j in  load_file_res.items():
#     print i,j

# 逐行读取文本内容，两种方法不能同时调用
f = open('seq.txt','r')
# print f.read()
# print type(f.readlines()),type(f.readline())
# print f.readlines(),f.read()
for i in f.readlines():
    print i

print "#"
while True:
    line = f.readline()
    if  not line:
        break
    print line

