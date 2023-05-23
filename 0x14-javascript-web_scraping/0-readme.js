#!/usr/bin/node
//This script is used to read the contents of a file(in utf)

const file = process.argv[2];
const fs = require('fs');

fs.readFile(file, 'utf8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
