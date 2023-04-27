#!/bin/bash
# script that sends a json POST request to a url passedas the first arg and displays the body of the response
curl -sL -X POST -H "Content-Type: application/json" -d @"$2" "$1"
