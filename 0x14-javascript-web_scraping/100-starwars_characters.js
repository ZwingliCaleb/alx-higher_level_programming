#!/usr/binn/node
//This script prints all characters of the startwars movie

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(`Error: ${error.message}`);
  } else {
    const movie = JSON.parse(body);
    const characters = movie.characters;

    // This function fetches character details
    const fetchCharacter = (characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            reject(`Error: ${error.message}`);
          } else {
            const character = JSON.parse(body);
            resolve(character.name);
          }
        });
      });
    };

    // This function fetches  details for all characters
    Promise.all(characters.map(fetchCharacter))
      .then((characterNames) => {
        characterNames.forEach((characterName) => {
          console.log(characterName);
        });
      })
      .catch((error) => {
        console.log(error);
      });
  }
});

