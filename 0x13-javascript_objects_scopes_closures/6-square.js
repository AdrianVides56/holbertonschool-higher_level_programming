#!/usr/bin/node
const supSquare = require('./5-square');

class Square extends supSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      let i;
      for (i = 0; i < this.height; i++) {
        console.log(String(c).repeat(this.width));
      }
    }
  }
}
module.exports = Square;
