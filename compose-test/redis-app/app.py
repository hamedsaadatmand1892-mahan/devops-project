import redis

r = redis.Redis(host="redis", port=6379)

r.set("message", "Hello from Redis!")

print(r.get("message").decode())
