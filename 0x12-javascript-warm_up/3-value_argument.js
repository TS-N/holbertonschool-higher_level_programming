#!/usr/bin/node
const argList = process.argv;
let i = 2;
if (argList[2]) {
  while (argList[i]) {
    console.log(argList[i]);
    i++;
  }
} else {
  console.log('No argument');
}
