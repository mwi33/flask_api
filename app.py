# import flask libraries
from flask import Flask, render_template

# create an instance of the class
app = Flask(__name__)

data = [
    {
        'name':'Bill',
        'place':'Perth',
        'id':'12345'
    },
    {
        'name':'Jane',
        'place':'Sydney',
        'id':'6789'
    },
    {
        'name':'James',
        'place':'Melbourne',
        'id':'1092'
    }
]

# the app.route decorator is used to tell flask what URL should trigger the function
# this route and function are for when the site index page (/) is accessed with a GET request
@app.route('/')
def hello():
    return render_template('index.html', data=data)



if __name__ == '__main__':
    app.run(host='0.0.0.0')