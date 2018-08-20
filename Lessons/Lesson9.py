# olexandrit:~/workspace (master) $ sudo service redis-server start
# Starting redis-server: redis-server.
# olexandrit:~/workspace (master) $ redis-c
# redis-check-aof   redis-check-dump  redis-cli         
# olexandrit:~/workspace (master) $ redis-c
# redis-check-aof   redis-check-dump  redis-cli         
# olexandrit:~/workspace (master) $ sudo redis-cli                                                                                                                                                                                                                  
# 127.0.0.1:6379> 
# 127.0.0.1:6379> ping 
# PONG
# 127.0.0.1:6379> set alex 1103
# OK
# 127.0.0.1:6379> get alex
# "1103"

import redis

r_server = redis.Redis(host="127.0.0.1",port=6379)

# r_server.delete("alex")
# r_server.delete("foo")

# r_server.set("alex",1000)
# key_get = r_server.get("alex")

# print(key_get)

# r_server.incr("alex")
# print(r_server.get("alex"))

# r_server.incr("alex",102)
# print(r_server.get("alex"))

# r_server.lpush("foo",*[1,2,3,4])
# print(r_server.lrange("foo",0,-1))

# r_server.rpush("foo",0)
# print(r_server.lrange("foo",0,-1))

# print(r_server.lindex("foo",0))

r_server.flushall()

# r_server.delete("set1")
# r_server.sadd("set1",1)
# r_server.sadd("set1",2)
# r_server.sadd("set1",3)
# r_server.sadd("set1",4)
# r_server.sadd("set2",1)
# r_server.sadd("set2",1)
# r_server.sadd("set2",2)
# r_server.sadd("set3",5)
# r_server.sadd("set3",5)
# r_server.sadd("set3",1)


print("set1:{}\set2:{}\set3:{}".format(r_server.smembers("set1"),r_server.smembers("set2"),r_server.smembers("set3")))
# print(r_server.sismember("set1",5))