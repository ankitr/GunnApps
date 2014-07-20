#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    A hack to validate a name-studentid pair by looking at the mail
    system's error codes. Essentially, we send an SMTP signal, which
    fails if the id is incorrect.
"""

import socket
import urllib2
import json

HOST = 'palo-alto.edu';

# This is an API call to get the MX records from the
# host. It's hardcoded in below because efficiency is a thing.
#
# info = urllib2.urlopen('http://dns-api.org/mx/' + HOST)
# data = json.load(info)
# info.close()
#
# mail = data[0]['exchange']

mail = 'aspmx.l.google.com'

TCP_IP = socket.gethostbyname(mail)
TCP_PORT = 25 # SMTP happens on 25.

BUFFER_SIZE = 80 # Messages longer than that are cause for concern.

def testemail(name):
    """
        Test a name to see if that email exists.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.recv(BUFFER_SIZE)

    # identify yourself as a legit thing.
    s.send("HELO " + socket.gethostname() + "\n")
    s.recv(BUFFER_SIZE) # flush buffer

    # Yo, we're us, and we're sending mail.
    s.send("MAIL From: <verifier@%s>\n" % socket.gethostname())
    s.recv(BUFFER_SIZE) # flush buffer

    # We're aiming for this dude.
    s.send("RCPT To: <%s@%s>\n" % (name, HOST))

    # 250 is SMTPese for yay.
    answer = '250' in s.recv(BUFFER_SIZE)
    s.close()
    return answer

def verifyid(first, last, id):
    """
        Verify a name-id pair.
    """
    return testemail("%s.%s.%s" % (
        first.lower(),
        last[0].lower(),
        str(id)[3:]) # strip out `950`.
    )
