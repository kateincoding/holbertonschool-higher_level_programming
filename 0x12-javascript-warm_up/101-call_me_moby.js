#!/usr/bin/node
//  function that executes x times a function.
function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}
exports.callMeMoby = callMeMoby;
