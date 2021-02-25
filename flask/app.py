from flask import Flask
import os
from redis import Redis

master = Redis(host='redis-master', port=6379)
slave = Redis(host='redis-slave', port=6379)
app = Flask(__name__)

# This is not intended to be particuarly interesting as an app
@app.route('/')
def hits():
    master.incr('hits')
    hits = int(slave.get('hits'))
    print(f"hits: {hits}")
    return f"Hits counter: {hits}"

if __name__ == "__main__":
    print("main(v2)")
    master.set('hits', 0)
    print("run()")
    app.run(host='0.0.0.0', port=80)
