#!/usr/bin/node
// function that prints the number of arguments already printed and the new argument value

exports.logMe = (function (item) {
  let n = 0;
  function print (item) {
    console.log(`${n}: ${item}`);
    n++;
  }
  return print;
}());
