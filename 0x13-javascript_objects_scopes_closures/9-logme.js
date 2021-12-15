#!/usr/bin/node
// function that prints the number of arguments already printed and the new argument value
let counter = 0;
exports.logMe = function (item) {
  return console.log(`${counter++}: ${item}`);
};
