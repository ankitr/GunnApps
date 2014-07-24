#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bson.objectid import ObjectId

from .. import db

def new_session(app_id, user_id):
    """Creates a new session and returns the session token for the app."""
    user = db.users.one({'student_id': int(user_id)})
    app = db.apps.one({'_id': ObjectId(app_id)})
    # TODO(@ankitr): Finish this.
