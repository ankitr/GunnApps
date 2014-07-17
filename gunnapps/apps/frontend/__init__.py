#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Ankit Ranjan'
__version__ = 'v0.1'

from flask import jsonify
from flask import render_template
from flask import request

from .. import factory
#from ..logs import log

import assets

def create_app(debug=False):
    """Returns the Gunn Apps front-end application instance."""

    app = factory.create_app(__name__, __path__, debug=debug)

    # Init assets
    # assets.init_app(app)

    # Setup front-end logging.
    # @app.before_request
    # def log_request():
    #     log.debug('Front-end request from %s to location %s' % (request.remote_addr, request.path))

    # Register error handlers for exceptional cases.
    app.errorhandler(404)(_on_404)
    app.errorhandler(500)(_on_500)

    return app


def _on_404(e):
    # log.debug(e)
    return render_template('error/404.html'), 400

def _on_500(e):
    # log.error(e)
    return jsonify(Error='Server error.'), 500
