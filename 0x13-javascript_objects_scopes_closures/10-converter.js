#!/usr/bin/node
exports.converter = function (base) {
  return function (number) {
    return (parseInt(String(number)).toString(base));
  };
};
