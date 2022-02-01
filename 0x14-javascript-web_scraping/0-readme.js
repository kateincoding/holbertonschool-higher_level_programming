#!/usr/bin/node
const filename = process.argv[2];
const fs = require('fs');

fs.readFile(filename, function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data.toString('utf8'));
});
