#!/usr/bin/python3
""" This script fetches https://alx-intranet.hbtn.io/status """

import urllib.request as req

if __name__ == "__main__":
    with req.urlopen("https://alx-intranet.hbtn.io/status") as url:
        if url.readable():
            response = url.read()
            print("Body response:")
            print("\t- type: {}".format(type(response)))
            print("\t- content: {}".format(response))
            print("\t- utf8 content: {}".format(response.decode("utf-8")))
