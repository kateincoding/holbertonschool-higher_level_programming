#!/usr/bin/node
const movieID = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieID;
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const characterList = JSON.parse(body).characters;
    for (const characterUrl of characterList) {
      request(characterUrl, function (error, response, body) {
        if (error) {
          console.error('error:', error);
        } else {
          const peopleJson = JSON.parse(body);
          console.log(peopleJson.name);
        }
      });
    }
  }
});
