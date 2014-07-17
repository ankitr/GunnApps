#!/usr/bin/env python
# -*- coding: utf-8 -*-

from werkzeug.wsgi import DispatcherMiddleware

from flask import Flask

from apps import main 
from apps import api

app = Flask(__name__)

# This allows for nice URL segmenting and abstraction layers.
app.wsgi_app = DispatcherMiddleware(main.create_app(), {
    '/api': api.create_app()
})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
