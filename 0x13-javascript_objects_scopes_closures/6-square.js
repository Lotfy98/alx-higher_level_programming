#!usr/bin/node
const SquareParent = require('./5-square');

class Square extends SquareParent {
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
