#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charprint (x) {
    if (x === undefined) {
	    x = 'X';
    }
    for (let i = 0; i < this.hegight; i++) {
      let s = '';
      for (let y = 0; y < this.width; y++) {
        s += x;
      }
      console.log(s);
    }
  }
}
module.exports = Square;
