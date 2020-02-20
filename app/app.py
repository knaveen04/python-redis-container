import os

from flask import Flask
from redis import Redis


app = Flask(__name__)
bind_port = os.environ['BIND_PORT']
REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = os.environ['REDIS_PORT']

redis = Redis(host=REDIS_HOST, port=REDIS_PORT)


@app.route('/')
def web_counter():
    redis.incr('counter')
    return 'This is the {} visitor'.format(redis.get('counter'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
