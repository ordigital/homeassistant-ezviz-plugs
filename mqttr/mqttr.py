#!/usr/bin/python

import sys, json
from types import SimpleNamespace
sys.path.insert(0, './inc')

# when lack of proper input
def show_error(error_text):
    print(error_text)
    exit()

# if no arguments
if len(sys.argv) < 2:
    show_error("No JSON given as argument.")

# if not JSON format
try:
    payload = json.loads(sys.argv[1], object_hook=lambda d: SimpleNamespace(**d))
except ValueError as e:
    show_error("Bad JSON.")

try:
    # file must exist and have serve(payload) function
    service = __import__(payload.serve)
    service.serve(payload)
except Exception as e:
    show_error("Cannot find service file or function.")
