#!/usr/bin/node
// This is a script that prints all the characters of the starwars movie as well

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Status:', response.statusCode);
  } else {
    const movie = JSON.parse(body);
    const characterUrls = movie.characters;

    const fetchCharacter = (characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            reject(error);
          } else if (response.statusCode !== 200) {
            reject(`Status: ${response.statusCode}`);
          } else {
            const character = JSON.parse(body);
            resolve(character.name);
          }
        });
      });
    };

    const characterPromises = characterUrls.map(fetchCharacter);

    Promise.all(characterPromises)
      .then((characterNames) => {
        characterNames.forEach((characterName) => {
          console.log(characterName);
        });
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }
});

