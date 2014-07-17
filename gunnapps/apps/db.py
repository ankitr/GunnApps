#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

from mongokit import Connection
from mongokit import Document


# Create the MongoDB 
connection = Connection()

# Link the Auth DB.
auth = connection.auth
users = auth.users


@connection.register
class User(Document):
    """The user model for the DB."""

    __collection__ = 'users'
    __database__ = 'auth'

    structure = {
        'email': basestring,
        'password': basestring,
        'name': basestring,
        'registration': datetime.datetime,
        'tokens': [basestring]
    }

    required_fields = ['email', 'name', 'password']

    default_values = {
        'registration': datetime.datetime.utcnow,
        'tokens': []
    }

    def is_authenticated(self):
        # TODO: Consider changing.
        return True

    def is_active(self):
        # TODO: Consider changing.
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self['_id'])