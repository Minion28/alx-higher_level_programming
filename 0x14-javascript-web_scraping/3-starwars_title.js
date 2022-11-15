#!/usr/bin/node
//print starwars movie where episode number matches given integer

const request = require('request');
const id = process.argv[2];

const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request(url, (error, resp, body) => {
  if (error)
  {
    console.log(error);
  }
  else
  {
    console.log(JSON.parse(body).title);
  }
  });
