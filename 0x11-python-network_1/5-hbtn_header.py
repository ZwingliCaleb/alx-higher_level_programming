#!/usr/bin/python3
''' script that takes URL and sends a request to the URL and displays the value of the variable.'''

import requests as req
import sys

if __name__ == "__main__":
    dat = req.get(sys.argv[1])
    dat1 = dat.headers.get('X-Request-Id')
    print(dat1)
