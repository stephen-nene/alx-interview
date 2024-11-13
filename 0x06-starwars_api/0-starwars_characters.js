#!/usr/bin/env node

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];
if (!movieId) {
  console.log("Please provide a movie ID as an argument.");
  process.exit(1);
}

// URL for the specified Star Wars movie using the movie ID
const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

// Fetch the movie details
request(movieUrl, (error, response, body) => {
  if (error) {
    console.error("Error fetching movie details:", error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error("Failed to retrieve movie data:", response.statusCode);
    return;
  }

  // Parse the JSON response
  const movieData = JSON.parse(body);
  const characterUrls = movieData.characters;

  // Iterate over each character URL and fetch their name
  characterUrls.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error("Error fetching character details:", error);
        return;
      }
      if (response.statusCode !== 200) {
        console.error("Failed to retrieve character data:", response.statusCode);
        return;
      }

      // Parse and print the character's name
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
