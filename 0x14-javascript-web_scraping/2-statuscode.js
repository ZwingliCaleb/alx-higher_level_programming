#!/usr/bin/node
//This is a script that displays a status code of a GET request

const request = require('request');
const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.log(`Error: ${error.message}`);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});

