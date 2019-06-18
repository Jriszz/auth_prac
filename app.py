from flask import Flask,request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from auth import verify
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key here'
app.register_blueprint(verify)

if __name__ == '__main__':
    app.run()