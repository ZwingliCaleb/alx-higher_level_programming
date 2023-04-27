#!/bin/bash
# script that  takes in a URLas an arg, sends GET request to URL and display body of response
curl -sH "X-School-User-Id: 98" "$1"
