#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charprint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.hegight; i++) {
      let s = '';
      for (let y = 0; y < this.width; y++) {
        s += c;
      }
      console.log(s);
    }
  }
}
module.exports = Square;
