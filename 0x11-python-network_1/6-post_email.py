#!/usr/bin/python3
''' Script that takes in a URL and an email address sends a POST request to the passed URL with email as parameter '''

import requests as req
import sys

if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    dat = req.post(sys.argv[1], data=email)
    print(dat.text)
