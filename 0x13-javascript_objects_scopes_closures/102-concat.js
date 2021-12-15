#!/usr/bin/node
//  script that concats 2 files

const { argv } = require('process');
const fs = require('fs');

const file1 = fs.readFileSync(argv[2]);
const file2 = fs.readFileSync(argv[3]);
fs.writeFileSync(argv[4], file1 + file2);
