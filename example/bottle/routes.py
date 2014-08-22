from example.bottle.bttl import Bottle

app = Bottle()

@app.get('/')
def index():
    return "Hello, World!"

@app.get('/orders')
def get_orders():
    return "<h1>All Current Orders:</h1>"

@app.post('/order')
def post_order():
    return "<h1>Order placed.</h1>"

@app.get('/order/<id>')
def get_order(id):
    return "<h2>Order " + id + " is not ready.</h2>"

@app.put('/order/<id>')
def put_order(id):
    return "<h2>Received update for Order " + id + ".</h2>"

@app.delete('/order/<id>')
def delete_order(id):
    return "<h2>All done with Order " + id + "; removed.</h2>"

@app.options('/order/<id>')
def options_order(id):
    return "<h2>That order is allowed to...</h2>"

@app.get('/payment/order/<id>')
def get_payment_order(id):
    return "<h2>Payment Status</h2>"

@app.put('/payment/order/<id>')
def put_payment_order(id):
    return "<h2>Paid for Order " + id + ".</h2>"

@app.options('/payment/order/<id>')
def options_payment_order(id):
    return "<h2>That payment can be ...</h2>"
