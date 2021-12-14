#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments

const { argv } = require('process');
const argc = argv.length - 2;
let max = 0;
let second = 0;
if (argc >= 2) {
  max = argv[2];
  second = argv[3];
  for (let i = 1; i <= argc; i++) {
    if (argv[i + 2] > max) {
      second = max;
      max = argv[i + 2];
    }
  }
}
console.log(`${second}`);
