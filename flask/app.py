from flask import Flask
import os
from redis import Redis

redis = Redis(host=os.getenv('REDIS_HOST', 'localhost'),
              port=os.getenv('REDIS_PORT', 6379))
app = Flask(__name__)

# This is not intended to be particuarly interesting as an app
@app.route('/')
def hello():
    redis.incr('hits')
    hits = int(redis.get('hits'))
    return f"hits counter: {hits}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
