#!/usr/bin/node
//  class Square that defines a square and inherits from Square of 5-square.js
const SquarePrev = require('./5-square');

class Square extends SquarePrev {
  charPrint (c) {
    const x = !c ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      console.log(x.repeat(this.width));
    }
  }
}

module.exports = Square;
