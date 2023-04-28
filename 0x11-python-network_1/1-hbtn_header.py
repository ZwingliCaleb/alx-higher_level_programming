#!/usr/bin/python3
# script that takes in a URL sends a request to the URL and displays the value of x-Request-Id variable found in the header of the response

import urllib.request as req
import sys

if __name__ == "__main__":
    with req.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request_Id'))
