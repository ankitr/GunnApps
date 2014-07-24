#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request 

from utils import responses

from ..utils import sessions

import db


blueprint = Blueprint('api', __name__)


@blueprint.route('/', methods=['GET'])
def land():
    """Wait, what are you doing here?"""
    return responses.success('Welcome to the GunnApps API. Enjoy your stay!')
