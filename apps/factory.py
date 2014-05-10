#!/usr/bin/env python
# -*- coding: utf-8 -*-

import importlib
import pkgutil

from flask import Blueprint
from flask import Flask


def register_blueprints(app, package_name, package_path):
    """Register all Blueprint instances on the specified Flask application found
    in all modules for the specified package.

    :param app: the Flask application
    :param package_name: the package name
    :param package_path: the package path
    """
    rv = []
    for _, name, _ in pkgutil.iter_modules(package_path):
        m = importlib.import_module('%s.%s' % (package_name, name))
        for item in dir(m):
            item = getattr(m, item)
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
            rv.append(item)
    return rv


def create_app(package_name, package_path, debug=False):
    """Returns a :class:`Flask` application instance configured with common
    functionality for the platform.

    :param package_name: application package name
    :param package_path: application package path
    :param settings_override: a dictionary of settings to override
    """

    app = Flask(package_name, static_folder='static', static_url_path='')
    app.debug = debug
    app.secret_key = 's3cr3t'

    app.config.from_pyfile('settings.cfg', silent=True)

    register_blueprints(app, package_name, package_path)

    return app