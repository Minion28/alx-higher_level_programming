#!/usr/bin/node
const list = require('./100-data').list;
const m = list.map(function (value, index) { return value * index;});
console.log(list);
console.log(m);
