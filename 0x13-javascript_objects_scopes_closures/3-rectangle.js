#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let x = 0;
    let e = 0;

    while (x < this.height) {
      let y = '';
      while (e < this.width) {
        y += 'X';
        e++;
      }
      x++;
      console.log(y);
    }
  }
}

module.exports = Rectangle;
