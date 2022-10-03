#!/usr/bin/node
const fArg = process.argv[2];
if (fArg === undefined) {
  console.log('No argument');
} else {
  console.log(fArg);
}
