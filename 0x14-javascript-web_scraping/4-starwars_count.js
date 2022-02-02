#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
const id = '18';

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const jsonBody = JSON.parse(body);
    let counter = 0;
    for (const res of jsonBody.results) {
      for (const char of res.characters) {
        if (char.search(id) > 0) {
          counter++;
        }
      }
    }
    console.log(counter);
  }
});
