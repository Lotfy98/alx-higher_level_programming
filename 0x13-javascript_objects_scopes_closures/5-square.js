#!/usr/bin/node
const Rectangle = required('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
	  super(size, size);
  }
}
module.exports = Square;
