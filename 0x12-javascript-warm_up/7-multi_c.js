#!/usr/bin/node
// script that prints x times “C is fun”
const { argv } = require('process');

let i = 0;
do {
  console.log('C is fun');
  i++;
} while (i < argv[2]);
