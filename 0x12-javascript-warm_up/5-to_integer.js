#!/usr/bin/node
const conv = parseInt(process.argv[2]);
if (isNaN(conv)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + conv);
}
