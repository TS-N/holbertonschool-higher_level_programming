#!/usr/bin/node
exports.esrever = function (list) {
  const revList = [];
  let i;
  for (i = list.length - 1; i >= 0; i--) {
    revList.push(list[i]);
  }
  return (revList);
};
