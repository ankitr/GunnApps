#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Ankit Ranjan'
__version__ = 'v0.1'

from flask import jsonify
from flask import request

from werkzeug.exceptions import BadRequest
from werkzeug.exceptions import Unauthorized

from .. import factory
from ..logs import log

from responses import error

def create_app(debug=False, database=None):
    """Returns the Gunn Apps API application instance."""

    app = factory.create_app(__name__, __path__, debug=debug)

    if database: app.config['DATABASE'] = database

    # Setup API logging.
    @app.before_request
    def log_request():
        log.debug('API request from %s to location %s. Parameters: %s'
            % (request.remote_addr, request.path, request.values.to_dict()))

    # Register error handlers for exceptional cases.
    app.errorhandler(400)(_on_400)
    app.errorhandler(401)(_on_401)
    app.errorhandler(404)(_on_404)
    app.errorhandler(405)(_on_405)
    app.errorhandler(500)(_on_500)

    return app

def _on_400(e):
    log.debug(repr(e))
    return error('Bad request.')

def _on_401(e):
    log.warn(repr(e))
    return error('Not authorized.', 401)

def _on_404(e):
    log.debug(repr(e))
    return error('Not found.', 404)

def _on_405(e):
    log.debug(repr(e))
    return error('Method not allowed.', 405)

def _on_500(e):
    log.exception('HTTP 500 Served.')
    return error('Server error.', 500)