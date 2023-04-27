#!/bin/bash
# Bash script taking url sends GET request to the URL and displays body of the response

if [ $# -eq 0 ]; then
  echo "Error: URL argument not provided"
  exit 1
fi

response=$(curl -s -X GET $1)
if [ $(echo "$response" | grep -c 'HTTP/1\.[01] 200') -eq 0 ]; then
  echo "Error: Could not retrieve URL or status code was not 200"
  exit 1
fi

echo "$response"

