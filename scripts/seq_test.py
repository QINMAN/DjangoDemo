# coding:utf-8

import json

dict = {'name':'秦曼', 'gender':'female'}

# 序列化
dump_res = json.dumps(dict, ensure_ascii=False)
print dump_res, type(dump_res)

# 序列化到文件
dump_file_res = json.dump(dict, open('seq.txt','w'), ensure_ascii=False)
print dump_file_res, type(dump_file_res)

# 反序列化
load_res = json.loads(dump_res)
print load_res, type(load_res)

# 对文件中的数据反序列化
load_file_res = json.load(open('seq.txt','r'))
print load_file_res, type(load_file_res)