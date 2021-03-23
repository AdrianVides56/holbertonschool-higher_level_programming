#!/usr/bin/node
exports.converter = function (base) {
  return function newNum (num) {
    return num.toString(base);
  };
};
