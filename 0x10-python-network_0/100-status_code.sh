#!/bin/bash
# script to send request to URL passed as an arg and display status code of response
curl -s -o /dev/null -w "%{http_code}" "$1"
