import redis

pool = redis.ConnectionPool(host='127.0.0.1',port='6379')
client = redis.Redis(connection_pool=pool)
zhengzuang = client.hgetall('zhengzuang')
for k  in zhengzuang:
    print(k.decode('utf-8')+"    "+zhengzuang.get(k).decode('utf-8'))