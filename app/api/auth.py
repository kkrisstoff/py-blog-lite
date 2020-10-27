from flask import g, jsonify, request
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask_babel import _
from app.models import User
from app.api.errors import error_response
from app.api import bp
from app import db

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()


@basic_auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user


@basic_auth.error_handler
def basic_auth_error(status):
    return error_response(status)


@token_auth.verify_token
def verify_token(token):
    return User.check_token(token) if token else None


@token_auth.error_handler
def token_auth_error(status):
    return error_response(status)


# API
@bp.route('/v0/login', methods=['POST'])
def login_api():
    data = request.json
    username = data['username']
    password = data['password']
    user = verify_password(username, password)
    if not user:
        return jsonify({
            'username': None,
            'error': True,
            'errorMessage': _('Invalid username or password')
        })
    res = user.to_dict(include_links=False, include_email=True)
    res['token'] = user.get_token()
    # TODO: don't sure I need it
    # db.session.commit()
    return jsonify(res)
