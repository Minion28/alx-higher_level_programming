#!/usr/bin/node
let slarge = process.argv.slice(2).map((x) => {
  return parseInt(x);
});

if (slarge.length <= 1) {
  console.log(0);
} else {
  console.log(slarge.sort((a, b) => {
    return b - a;
  })[1]);
}
