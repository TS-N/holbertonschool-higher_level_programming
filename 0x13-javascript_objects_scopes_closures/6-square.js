#!/usr/bin/node
const Squar = require('./5-square');
class Square extends Squar {
  charPrint (c) {
    let i;
    if (!c) {
      c = 'X';
    }
    for (i = 0; i < this.width; i++) {
      console.log(c.repeat(this.height));
    }
  }
}

module.exports = Square;
