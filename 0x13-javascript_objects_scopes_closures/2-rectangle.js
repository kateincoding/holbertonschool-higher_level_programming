#!/usr/bin/node
// class Rectangle that defines a rectangle with a side > 0

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.height = h;
      this.width = w;
    }
  }
}
module.exports = Rectangle;
