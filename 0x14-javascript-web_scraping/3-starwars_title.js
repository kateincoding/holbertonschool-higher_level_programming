#!/usr/bin/node
const episode = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + episode;
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
