from flask import Flask, jsonify

app = Flask(__name__)
stores = [
    {
        "name": "My Wonderful Store",
        "items": [
            {
                "name": "My Item",
                "price": 15.99
            }
        ]
    }
]

# Creating a basic endpoint for the home route
# app.route() is basically like a function wrapper
# function name doesn't actually matter
@app.route('/')
def home():
    return "Hello, world!"


app.run(port=5000)

# POST /store
# only accessible via POST, but could have more
@app.route('/store', methods=['POST'])
def create_store():
    pass

# GET /store/:name
@app.route('/store/<string:name>', methods=["GET"])
def get_store(name):
    pass

# GET /store
@app.route('/store', methods=["GET"])
def get_stores():
    pass

# POST /store/:name/item
@app.route('/store/<string:name>/item', methods=["POST"])
def create_item_in_store(name):
    pass

# GET /store/:name/item
@app.route('/store/<string:name>/item', methods=["GET"])
def get_items_in_sote(name):
    pass
