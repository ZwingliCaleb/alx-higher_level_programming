#!/usr/bin/python3
''' script that takes 2 arguments to solve challenge; list 10 commits '''

import requests as req
import sys

if __name__ == "__main__":
    dat = req.get("https://api.github.com/repos/{}/{}/commits"
                  .format(sys.argv[2], sys.argv[1]))

    commits = dat.json()
    for c in commits[:10]:
        print(c.get('sha'), end=': ')
        print(c.get('commit').get('author').get('name'))
