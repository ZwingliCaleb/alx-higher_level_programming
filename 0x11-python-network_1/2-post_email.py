#!/usr/bin/python3
# This is a script to take a URL and email sends a POST request to the passedURL with email as parameter and displays body of response

import urllib
import urllib.request as req
import urllib.parse as parse
import sys

if __name__ == "__main__":
    raw_mail = {'email': sys.argv[2]}
    data = parse.urlencode(raw_mail)
    data = data.encode('utf-8')
    request = req.Request(sys.argv[1], data)
    with req.urlopen(request) as response:
        print(response.read().decode('utf-8'))
