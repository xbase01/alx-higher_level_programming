#!/usr/bin/node
// Executes theFunction 'x' number of times


exports.callMeMoby = function (x, theFunction) {
    while (x-- > 0) {
	theFunction();
    }
};
