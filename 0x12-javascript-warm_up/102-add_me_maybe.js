#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) theFunction();
};

root@328cec1af55f:/alx-higher_level_programming/0x12-javascript-warm_up# cat 102-add_me_maybe.js
#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
