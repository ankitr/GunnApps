#!/usr/bin/env python
# -*- coding: utf-8 -*-

from werkzeug.wsgi import DispatcherMiddleware

from flask import Flask

from apps import main
from apps import api
from apps import discourse

app = Flask(__name__)

app.wsgi_app = DispatcherMiddleware(main.create_app(), {
    '/api': api.create_app()
})

if __name__ == '__main__':
    app.run()