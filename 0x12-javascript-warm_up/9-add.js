#!/usr/bin/node
// script that prints the addition of 2 integers

const { argv } = require('process');
const n = parseInt(argv[2]);
const m = parseInt(argv[3]);

if (isNaN(n) || isNaN(m)) {
  console.log('NaN');
} else {
  console.log(`${n + m}`);
}
