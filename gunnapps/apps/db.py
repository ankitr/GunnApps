#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import string

from mongokit import Connection
from mongokit import Document

from bson.objectid import ObjectId

# Create the MongoDB 
connection = Connection()

# Link the Auth DB.
auth = connection.auth
users = auth.users
apps = auth.apps

@connection.register
class User(Document):
    """The user model for the DB."""

    __collection__ = 'users'
    __database__ = 'auth'

    structure = {
        'student_id': int,
        'email': basestring,
        'password': basestring,
        'name': basestring,
        'pronoun': basestring,
        'registration': datetime.datetime,
        'tokens': [basestring]
    }

    required_fields = ['student_id', 'email', 'name', 'password', 'pronoun']

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
        return unicode(self['student_id'])

    def get_student_email(self):
        # TODO: Check how PAUSD handles middle initials, etc.
        first_name = self['name'].split(' ')[0].lower()
        last_name = self['name'].split(' ')[-1].lower()
        last_initial = last_name[0]
        student_id_tail = str(self['student_id'])[-5:]
        email = '%s.%s.%s@palo-alto.edu' % (first_name, last_initial, student_id_tail)
        return email


@connection.register
class App(Document):
    """Third-party applications on our framework."""

    __collection__ = 'apps'
    __database__ = 'auth'

    structure = {
        'owner': ObjectId,
        'name': basestring,
        'id': basestring,
        'secret': basestring
    }
    
    required_fields = ['owner', 'name', 'id', 'secret']

    def _generate_secret(self):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for i in xrange(32))
    
    def refresh_secret(self):
        self['secret'] = self._generate_secret()
        self.save(validate=True)
        return self['secret']
