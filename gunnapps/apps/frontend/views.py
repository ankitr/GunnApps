#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib

from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request

from flask.ext.login import current_user
from flask.ext.login import LoginManager
from flask.ext.login import login_required
from flask.ext.login import login_user
from flask.ext.login import logout_user

import db
#from ..logs import log

from mongokit import MultipleResultsFound


blueprint = Blueprint('dashboard', __name__)

login_manager = LoginManager()


# Sets up Flask Login.
@blueprint.record_once
def on_load(state):
    login_manager.init_app(state.app)

@login_manager.user_loader
def load_user(userid):
    return db.users.User.one({'student_id': int(userid)})

@login_manager.unauthorized_handler
def unauthorized():
    return render_template('main.html', message='Please log in.')


# Creates our views.
@blueprint.route('/', methods=['GET'])
def land():
    """Returns the landing page."""
    if request.args.get('logout'):
        return render_template('main.html', message='Successfully logged out.')
    if current_user.is_authenticated():
        return render_template('loggedin.html', user=current_user)
    return render_template('main.html')

@blueprint.route('/', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    try:
        user = db.users.User.one({'email':email})
    except MultipleResultsFound as e:
        # log.critical('Multiple users with the same email address found!')
        # log.exception(e)
        pass
    if not user or (hashlib.sha512(password).hexdigest() != user['password']):
        return render_template('main.html', message='Incorrect credentials.',
                               email=email)
    login_user(user)
    return redirect('/', code=303)

@blueprint.route('/register', methods=['GET'])
def contemplate():
    """Returns the registration page."""
    return render_template('register.html')

@blueprint.route('/register', methods=['POST'])
def register():
    """Creates a user account."""
    # TODO: Consider removing this intermediate assignment.
    code = request.form['code']
    student_id = int(request.form['studentId'])
    email = request.form['email']
    name = request.form['name'].title()
    password = request.form['password']
    pronoun = request.form['pronoun']
    year = int(request.form['class'])
    if not db.codes.one({'code':code}):
        return render_template('register.html', message='Invalid code.',
                               name=name, email=email) #, student_id=student_id)
    if db.users.one({'email':email}) or db.users.one({'student_id':student_id}):
        # The user exists.
        return render_template('register.html', message='User already exists.',
                               name=name, email=email, student_id=student_id)
    # TODO(ankitr): Use email validation to ensure the user is real.
    # Remove the now-used code.
    db.codes.remove({'code':code})
    # Code is valid and user is free.
    user = db.users.User()
    # The student id is an int.
    user['student_id'] = student_id
    user['email'] = email
    user['name'] = name
    # Hashing the user password.
    user['password'] = hashlib.sha512(password).hexdigest()
    user['pronoun'] = pronoun
    user['year'] = year
    user.save()
    login_user(user)
    return redirect('/', code=303)

@blueprint.route('/logout')
@login_required
def logout():
    """Logs out the user."""
    logout_user()
    return redirect('/')

@blueprint.route('/about')
def about():
    return render_template('about.html')
