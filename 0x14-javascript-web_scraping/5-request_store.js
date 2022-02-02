#!/usr/bin/node
const url = process.argv[2];
const filename = process.argv[3];
const request = require('request');
const fs = require('fs');

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    fs.writeFile(filename, body, function (err) {
      if (err) throw err;
    });
  }
});
