import logging
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')
logging.basicConfig(filename='auth. log', level=logging. INFO)

@app.route('/')
def index():
    return render_template('login.html')
@app.route('/login', methods=[ 'POST' ])
def login():
    username = request.form['username']
    password = request.form['password']
    if password == 'mypassword':
        logging.info(f' {username} logged in successfully')
        return f'Welcome, {username}!'
    else:
        return 'Invalid password'
if __name__ == '__main__':
    app.run (host='46.101.199.136', port=8090, debug=True)
