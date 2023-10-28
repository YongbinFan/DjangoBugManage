import redis
from time import sleep
from django.conf import settings

conn = redis.Redis(host="192.168.0.7", port=6379, password=settings.REDIS_PASSWORD, encoding='utf-8')
conn.set('abc', '123', ex=10)
sleep(11)
value = conn.get('abc')
print(value)
