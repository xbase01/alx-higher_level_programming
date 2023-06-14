#!/usr/bin/node

// Prints a Rectangle with the parameters passed
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

  print () {
    if (!this.width || !this.height) {
	    return;
    }

    let rectangleString = '';

    for (let i = 0; i < this.height; ++i) {
	    rectangleString += 'X'.repeat(this.width) + '\n';
    }

    console.log(rectangleString);
  }
};
