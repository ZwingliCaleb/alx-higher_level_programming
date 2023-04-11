#!/usr/bin/node

const fInt = process.argv[2];
const sInt = process.argv[3];

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return (NaN);
  } else {
    return (parseInt(a) + parseInt(b));
  }

}
console.log(add(fInt, sInt));
