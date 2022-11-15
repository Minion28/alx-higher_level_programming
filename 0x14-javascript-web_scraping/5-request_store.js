#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const path = process.argv[3];

request(url, (error, resp, body) =>
{
  if (error) {
    return console.log(error);
  }

  fs.writeFile(path, body, 'utf8', (error) =>
  {
    if (error)
    {
      return console.log(error);
    }
  });
});
