#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let n = 0;
  let i;
  for (i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      n++;
    }
  }
  return (n);
};
