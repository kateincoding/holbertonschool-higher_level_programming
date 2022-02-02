#!/usr/bin/node
const movieID = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieID;
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const characterList = JSON.parse(body).characters;

    const length = characterList.length;
    CharacterRequest(0, characterList[0], characterList, length);
  }
});

function CharacterRequest (idx, urlChar, characters, limit) {
  if (idx === limit) { return; }
  request(urlChar, function (error, response, body) {
    if (!error) {
      const rbody = JSON.parse(body);
      console.log(rbody.name);
      idx++;
      CharacterRequest(idx, characters[idx], characters, limit);
    } else {
      console.error('error:', error);
    }
  });
}
