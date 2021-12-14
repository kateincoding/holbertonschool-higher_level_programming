#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments

const { argv } = require('process');
const argc = argv.length - 2;
let second = 0;
if (argc >= 2) {
  const numbers = [];
  for (let i = 0; i < argc; i++) {
    numbers.push(argv[i + 2]);
  }
  numbers.sort((a, b) => a - b);
  second = numbers[argc - 2];
}
console.log(`${second}`);
