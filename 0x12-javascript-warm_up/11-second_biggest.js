#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments

const { argv } = require('process');
const argc = argv.length - 2;
let max = 0;
let second = 0;
let i = 0;
do {
  i++;
  if (argv[i + 2] > argv[i + 2 - 1]) {
    second = max;
    max = argv[i + 2];
  }
} while (i <= argc);

console.log(`${second}`);
