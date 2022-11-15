#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, res, body) =>
{
  if (error)
  {
    return console.log(error);
  }

  let count = 0;
  const parsedBody = JSON.parse(body).results;

  for (let i = 0; i < parsedBody.length; i++)
  {
    const parse = parsedBody[i].characters.find((c) =>
    {
      c.match(/18/);
    });
    if (parse !== undefined)
    {
      count++;
    }
  }

  console.log(count);
});
