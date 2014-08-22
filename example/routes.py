from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Hello, World!"

@app.route('/orders', methods=['GET'])
def get_orders():
    return "<h1>All Current Orders:</h1>"

@app.route('/order', methods=['POST'])
def post_order():
    return "<h1>Order placed.</h1>"

@app.route('/order/<id>', methods=['GET'])
def get_order(id):
    return "<h2>Order " + id + " is not ready.</h2>"

@app.route('/order/<id>', methods=['PUT'])
def put_order(id):
    return "<h2>Received update for Order " + id + ".</h2>"

@app.route('/order/<id>', methods=['DELETE'])
def delete_order(id):
    return "<h2>All done with Order " + id + "; removed.</h2>"

@app.route('/order/<id>', methods=['OPTIONS'])
def options_order(id):
    return "<h2>That order is allowed to...</h2>"

@app.route('/payment/order/<id>', methods=['GET'])
def get_payment_order(id):
    return "<h2>Payment Status</h2>"

@app.route('/payment/order/<id>', methods=['PUT'])
def put_payment_order(id):
    return "<h2>Paid for Order " + id + ".</h2>"

@app.route('/payment/order/<id>', methods=['OPTIONS'])
def options_payment_order(id):
    return "<h2>That payment can be ...</h2>"
