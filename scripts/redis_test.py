#coding:utf-8
import redis
conn=redis.Redis(host="113.10.195.169",port=6379,password="zhou123456")
######   key - value ########
conn.set("test","zhou")
print conn.get("test")
conn.expire("test",10)
print conn.ttl("test")

###### hash  #######
conn.hset("test123","test","zhou")
print conn.hget("test123","test")

#######  list #####
conn.lpush("test22","zhou1")
conn.rpush("test22","abc")
print conn.lrange("test22",0,-1)

