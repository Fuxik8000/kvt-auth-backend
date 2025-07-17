import os
from flask import Flask, redirect, request, session, url_for, jsonify

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'changeme')

@app.route('/')
def index():
    return '<h2>Добро пожаловать!<br>Это backend авторизации.<br>OAuth Google/VK будет тут.</h2>'

# Заглушка для OAuth callback (именно сюда будет вести redirect)
@app.route('/oauth/callback')
def oauth_callback():
    # Сюда вернёт Google или VK после успешного входа
    code = request.args.get('code')
    return f'<h2>Авторизация успешна!<br>Ваш код: <b>{code}</b></h2>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
