#!/usr/bin/python3
''' script that takes github credentials and uses the github API to display id '''
import requests as req
import sys

if __name__ == "__main__":
    resp = req.get("https://api.github.com/user", auth=(
        sys.argv[1], sys.argv[2]))
    result = resp.json()
    print(result.get("id"))
