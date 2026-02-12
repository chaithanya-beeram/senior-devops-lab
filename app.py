from flask import Flask
import redis
import os

app = Flask(__name__)

# Connect to Redis using the Kubernetes Service name 'redis-service'
redis_pass = os.environ.get('REDIS_PASSWORD')

cache = redis.Redis(
    host='redis-service', 
    port=6379, 
    password=redis_pass  # Now it's secure!
)

@app.get('/')
def hello():
    # Increment the counter in Redis
    count = cache.incr('hits')
    return f"<h1>Hello from Kubernetes & Chaybeeram!</h1><p>I have been visited <b>{count}</b> times.</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)