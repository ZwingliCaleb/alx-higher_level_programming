#!/bin/bash
# bash scriptthat takes url sends a get request to the url and displays body of response
curl -s $1 | (read status; [ ${status:9:3} -eq 200 ] && cat)
