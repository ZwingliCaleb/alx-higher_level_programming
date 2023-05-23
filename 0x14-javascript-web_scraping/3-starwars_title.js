#!/usr/bin/node 
//This is a script to print the title of a starwars movie where the episode number matches a given integer

const request = require('request');
const moxieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request{url, (error, response, body) => {
	if (error){
		console.log(`Error: ${error.message}`);
	} else {
		const movie = JSON.parse(body);
		console.log(movie.title);
	}
});
