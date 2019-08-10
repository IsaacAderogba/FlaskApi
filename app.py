from flask import Flask

app = Flask(__name__)

# Creating a basic endpoint for the home route
# app.route() is basically like a function wrapper
@app.route('/') 
def home():
  return "Hello, world!"

app.run(port=5000)