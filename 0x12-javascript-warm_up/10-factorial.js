#!/usr/bin/node
function factorial (value) {
  if (value === 0 || isNaN(value)) {
    return (1);
  }
  return (value * factorial(value - 1));
}
const input = parseInt(process.argv[2]);
const result = factorial(input);
console.log(result);
