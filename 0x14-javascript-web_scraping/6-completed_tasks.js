#!/usr/bin/node
const url = process.argv[2];
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const jsonBody = JSON.parse(body);
    const dict = {};
    for (const task of jsonBody) {
      if (task.completed === true) {
        if (dict[task.userId] === undefined) {
          dict[task.userId] = 0;
        }
        dict[task.userId] += 1;
      }
    }
    console.log(dict);
  }
});
