#!/usr/bin/node
//  function that executes x times a function.
function callMeMoby (x, theFunction) {
  let i = 0;
  do {
    theFunction();
    i++;
  } while (i < x);
}
exports.callMeMoby = callMeMoby;
