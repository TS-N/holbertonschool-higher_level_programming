#!/usr/bin/node
const argList = process.argv;
if (argList[2]) {
  console.log(argList[2]);
} else {
  console.log('No argument');
}
