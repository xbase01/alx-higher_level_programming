#!/usr/bin/node

// Checks for Rectangle parameters
module.exports = class Rectangle {
  constructor (width, height) {
    if (this.isValidRectangle(width, height)) {
      this.width = width;
      this.height = height;
    }
  }

  isValidRectangle (width, height) {
    return typeof width === 'number' && typeof height === 'number' && width > 0 && height > 0;
  }
};
