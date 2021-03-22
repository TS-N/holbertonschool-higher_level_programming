#!/usr/bin/node
const avList = process.argv.slice(2);
const sortedList = avList.sort(function (a, b) { return b - a; });
if (avList.length <= 1) {
  console.log(0);
} else {
  console.log(sortedList[1]);
}
