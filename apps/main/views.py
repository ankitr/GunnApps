#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import jsonify
from flask import render_template
from flask import request

blueprint = Blueprint('dashboard', __name__)

@blueprint.route('/', methods=['GET'])
def land():
    """Returns the landing page."""
    return render_template('main.html')

@blueprint.route('/', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

@blueprint.route('/register', methods=['GET'])
@blueprint.route('/', methods=['GET'])
def contemplate():
    """Returns the registration page."""
    return render_template('register.html')