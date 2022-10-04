#!/usr/bin/node
const x = require('./101-data').dict;
const sort = {};
Object.keys(x).forEach(key => {
  if (sort[x[key]] === undefined) sort[x[key]] = [];
  sort[x[key]].push(key);
}
);
console.log(sort);
