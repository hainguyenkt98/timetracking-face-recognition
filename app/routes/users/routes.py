from flask import Blueprint, request, url_for, redirect, jsonify
from ...models import db, User

users = Blueprint('users', __name__)

@users.route('/', methods=['POST'])
def create_user():
    username = request.form['username']
    password = request.form.get('password')

    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    print ('Create new user sussessfull !')
    return jsonify(user.serialize)

@users.route('/<string:name>', methods=['GET'])
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('.hello_admin'))
    else:
        return redirect(url_for('.hello_guest', guest = name))

@users.route('/admin')
def hello_admin():
    return 'Hello Admin'

@users.route('/guest/<string:guest>')
def hello_guest(guest):
    return 'Hello %s' % guest