from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hellow, {}! Let\'s be buddies!</h1>'.format(name)

@app.route('/user-agent-info/')
def user_agent_info():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}'.format(user_agent)