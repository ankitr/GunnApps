#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    apps.api.responses
    ====================

    Helpful response functions for the API.
"""

import datetime
import json

from bson.objectid import ObjectId
from itertools import chain

from flask import Response

class APIEncoder(json.JSONEncoder):
    """Our own JSONEncoder because we're that cool."""
    def default(self, obj):
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.ctime()
        elif isinstance(obj, datetime.time):
            return obj.isoformat()
        elif isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)

def jsonify(data, status=200):
    return Response(json.dumps(data, cls=APIEncoder),
                    mimetype='application/json',
                    status=status)

def success(message, data={}):
    """Returns a Response with a success message and optional data."""
    try:
        data['Success'] = message
    except TypeError:
        data = dict(data)
        data['Success'] = message
    return jsonify(data)


def error(message, status=400):
    return jsonify({'Error':message}, status)