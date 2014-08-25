run-flask:
	gunicorn -w 10 -b 0.0.0.0:8080 -n gevent --pythonpath ./ \
	example.flask.routes:app

run-bottle:
	gunicorn -w 10 -b 0.0.0.0:8080 -n gevent --pythonpath ./ \
	example.bottle.routes:app
