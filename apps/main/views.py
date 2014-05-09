#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import jsonify
from flask import render_template
from flask import request

blueprint = Blueprint('dashboard', __name__)

@blueprint.route('/')
def hello():
    """Returns the landing page."""
    return render_template('main.html')