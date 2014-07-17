#!/usr/bin/env python

# NOTE: This will be changed, and probably put under a _run directory.
#       For now, do not import from this file.

import logging

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Main Log
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# Create debug.log handler
debug_handler = logging.FileHandler('/var/log/gunnapps/debug.log')
debug_handler.setLevel(logging.DEBUG)
debug_handler.setFormatter(formatter)

# Create info.log handler
info_handler = logging.FileHandler('/var/log/gunnapps/info.log')
info_handler.setLevel(logging.INFO)
info_handler.setFormatter(formatter)

# Create warning.log handler
# warning.log logs everything logging.ERROR and up.
warning_handler = logging.FileHandler('/var/log/gunnapps/warning.log')
warning_handler.setLevel(logging.WARNING)
warning_handler.setFormatter(formatter)

# Create error.log handler
# error.log logs everything logging.ERROR and up.
error_handler = logging.FileHandler('/var/log/gunnapps/error.log')
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)

# Create critical.log handlerre
# critical.log logs everything logging.ERROR and up.
critical_handler = logging.FileHandler('/var/log/gunnapps/critical.log')
critical_handler.setLevel(logging.ERROR)
critical_handler.setFormatter(formatter)

# Add handlers
log.addHandler(info_handler)
log.addHandler(debug_handler)
log.addHandler(warning_handler)
log.addHandler(error_handler)
log.addHandler(critical_handler)
