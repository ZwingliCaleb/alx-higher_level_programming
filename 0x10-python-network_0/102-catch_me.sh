#!/bin/bash
# script to make a request to a port that causes the server to respond with a message
curl -sLX PUT -d "user_id=98" 0.0.0.0:5000/catch_me --header "Origin: HolbertonSchool"
