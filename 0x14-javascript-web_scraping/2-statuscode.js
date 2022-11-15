#!/usr/bin/node
//display status code of a GET request

const url = process.argv[2];
const request = require('request');

request(url), function (error, resp, body) {
  if (error)
  {
    console.log('error:', error);
  }
  else
  {
    console.log('code: ', resp && resp.statusCode);
  }
};
