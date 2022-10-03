#!/usr/bin/node
const t = parseInt(process.argv[2]);
if (isNaN(t)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < t; i++) {
    console.log('C is fun');
  }
}
