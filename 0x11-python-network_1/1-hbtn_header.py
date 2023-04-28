#!/usr/bin/python3
# script that takes in a URL sends a request to the URL and displays the value of x-Request-Id variable found in the header of the response

import urllib.request
import sys

if len(sys.argv) > 1:
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(f"{x_request_id}")
else:
        print("Provide a URL as argument.")
