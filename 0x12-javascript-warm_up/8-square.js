#!/usr/bin/node
// script that prints a square
const { argv } = require('process');

let i = 0;
const n = 'X';
const num = parseInt(argv[2]);
if (isNaN(num)) {
  console.log('Missing size');
} else if (argv[2] > 0) {
  do {
    console.log(n.repeat(argv[2]));
    i++;
  } while (i < argv[2]);
}
