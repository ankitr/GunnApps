#!/usr/bin/env python

from __future__ import print_function

import string
import random
import pymongo

def generate_code(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for i in xrange(size))

def generate_codes(number=65536, length=8):
    codes = []
    for i in xrange(number):
        codes.append(generate_code(length))
    if len(codes) != number:
        # There are duplicates.
        return generate_codes(number, length)
    return codes

if __name__=='__main__':
    client = pymongo.MongoClient()
    db = client.auth
    codes = generate_codes()
    while codes:
        code = codes.pop()
        print('Inserting code %s.' % code)
        db.registration_codes.insert({'code':code})
    print('Completed code insertion.')
