from . import verify
from flask_httpauth import HTTPDigestAuth
from flask import abort

digestauth = HTTPDigestAuth()

users = {
    'susan':'hello',
    'Tom':'bye'
}
@digestauth.get_password
def get_password(username):
    if username in users:
        return users.get(username,'')
    abort(401)

@verify.route('/v/info/verify',methods=['GET'])
@digestauth.login_required
def userinfo():
    return 'Hell,%s!'% digestauth.username()