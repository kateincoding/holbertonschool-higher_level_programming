#!/usr/bin/node
const filename = process.argv[2];
const string = process.argv[3];
const fs = require('fs');

fs.writeFile(filename, string, function (err) {
  if (err) throw err;
});
