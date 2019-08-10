from flask import Flask, jsonify, request

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

# POST /store
# only accessible via POST, but could have more
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data['name'],
        "items": []
    }
    stores.append(new_store)
    return jsonify({"store": new_store})

# GET /store/:name
@app.route('/store/<string:name>', methods=["GET"])
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({"message": "Store not found"})

# GET /store
@app.route('/store', methods=["GET"])
def get_stores():
    return jsonify({"stores": stores})

# POST /store/:name/item
@app.route('/store/<string:name>/item', methods=["POST"])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                "name": request_data['name'],
                "price": request_data['price']
            }
            store['items'].append(new_item)
            return jsonify({"items": store["items"]})

    return jsonify({"message": "Error in posting new item"})

# GET /store/:name/item
@app.route('/store/<string:name>/item', methods=["GET"])
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({"items": store["items"]})
    return jsonify({"message": "Store not found"})


app.run(port=5000)
