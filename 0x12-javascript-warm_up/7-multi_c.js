#!/usr/bin/node
// script that prints x times “C is fun”
const { argv } = require('process');

let i = 0;
const num = parseInt(argv[2]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else if (argv[2] > 0) {
  do {
    console.log('C is fun');
    i++;
  } while (i < argv[2]);
}
