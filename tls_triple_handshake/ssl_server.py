import logging
from flask import Flask, render_template, request
import ssl

app = Flask(__name__, template_folder='templates')
logging.basicConfig(filename='auth.log', level=logging.INFO)

# Загрузка SSL сертификата и ключа
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile='server.crt', keyfile='server.key')

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if password == 'mypassword':
        logging.info(f'{username} logged in successfully')
        return f'Welcome, {username}!'
    else:
        return 'Invalid password'

if __name__ == '__main__':
    # Запуск сервера с SSL
    app.run(host='192.168.0.107', port=8090, debug=True, ssl_context=ssl_context)
