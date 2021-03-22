#!/usr/bin/node
const x = parseInt(process.argv[2]);
let i;
if (!isNaN(x)) {
  for (i = 0; i < x; i++) {
    console.log('X'.repeat(x))
  }
} else {
  console.log('Missing size');
}
