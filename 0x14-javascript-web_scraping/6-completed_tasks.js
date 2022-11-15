#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const store = {};
let x = '';

request(url, (error, resp, body) =>
{
  if (error)
  {
    return console.log(error);
  }

  const parse = JSON.parse(body);

  for (let a = 0; a < parse.length; a++)
  {
    x = parse[a].userId;
    if (parse[a].completed) {
      store[x] = (store[x] || 0) + 1;
    }
  }

  console.log(store);
});
