#!flask/bin/python
from flask import Flask

from pulsar.apps import wsgi
from pulsar.apps.wsgi.middleware import middleware_in_executor, wait_for_body_middleware

from werkzeug.wrappers import Response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Hello, World!"

class Site(wsgi.LazyWsgi):
    def setup(self, environ=None):
        return wsgi.WsgiHandler(
            [wait_for_body_middleware,
             middleware_in_executor(app)])

if __name__ == '__main__':
    wsgi.WSGIServer(
        callable=Site(),
        workers=0,
	thread_workers=20,
        bind='0.0.0.0:8080').start()
