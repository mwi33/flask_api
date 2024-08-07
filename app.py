# import flask libraries
from flask import Flask

# create an instance of the class
app = Flask(__name__)

# the app.route decorator is used to tell flask what URL should trigger the function
@app.route('/hello/')
def hello():
    return "Hello, World"

if __name__ == '__main__':
    app.run(host='0.0.0.0')