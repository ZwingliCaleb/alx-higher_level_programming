#!/usr/bin/node
//This is a script that prints the number of movies where the character "Wedge Antiles" is present

const request = require('request');
const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(`Error: ${error.message}`);
  } else {
    const films = JSON.parse(body).results;
    const count = films.filter((film) => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)).length;
    console.log(count);
  }
});

