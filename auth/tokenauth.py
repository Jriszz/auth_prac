from .import verify
from flask_httpauth import HTTPTokenAuth
from auth import verify
from flask import g,make_response
tokenauth = HTTPTokenAuth()

tokens = {
    'secret-token-1':'john',
    'secret-token-2':'susan'
}

@tokenauth.verify_token
def verify_token(token):
    if token in tokens:
        g.current_user = tokens[token]
        return True
    return False
@verify.route('/token',methods=['GET'])
@tokenauth.login_required
def verify_token():
    reponse = make_response()
    reponse.data= 'Congratulation you pass!'
    reponse.status_code =200
    return reponse
